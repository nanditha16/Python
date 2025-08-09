# Use Case: Cloud Cost Optimization — Lambda handle for Elastic IP clean-up using boto3.

# Overview:
# This AWS Lambda function helps run on a schedule (EventBridge) and drop its CSV report in S3.
# It will look through EC2 regions, find unassociated EIPs, and release them if eligible. 
# 1. Add filters to exclude EIPs used by NAT Gateways, Network Load Balancers, and Global Accelerator. 
# 2. NAT Gateways associate EIPs differently; the function tracks them via AllocationIds.
# 3. For Network Load Balancers, static IPs should be checked through NetworkInterfaceOwnerId, and also verify associations for EC2 addresses.
# 4. Global Accelerator support is planned via placeholder logic.
# 5. EIPs are filtered by age (MIN_AGE_DAYS) and excluded if tagged (e.g., DoNotDelete=true).
# 6. A dry-run mode (APPLY=false) allows safe testing before actual release.
# 7. A CSV report is generated and stored in S3 with full details of scanned, skipped, and released EIPs.
# 8. CloudWatch metrics are pushed for observability (CandidatesFound, Released).
# 9. Structured logging is used for auditability and debugging.
# 10. Timeout guard ensures Lambda exits gracefully before hitting execution limits.

# IAM Permissions Required (Lambda Execution Role):
# Ensure the Lambda role includes the following permissions:
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     { "Effect": "Allow", "Action": ["sts:GetCallerIdentity"], "Resource": "*" },
#     {
#       "Effect": "Allow",
#       "Action": [
#         "ec2:DescribeRegions",
#         "ec2:DescribeAddresses",
#         "ec2:DescribeNatGateways",
#         "ec2:ReleaseAddress"
#       ],
#       "Resource": "*"
#     },
#     {
#       "Effect": "Allow",
#       "Action": ["s3:PutObject"],
#       "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
#     },
#     {
#       "Effect": "Allow",
#       "Action": ["cloudwatch:PutMetricData"],
#       "Resource": "*"
#     }
#   ]
# }

# Environment Variables:
# Set these in the Lambda configuration to control behavior:
# - REGIONS — Comma-separated list of AWS regions to scan (optional; scans all if unset)
# - APPLY — Set to true to release EIPs; false for dry-run mode
# - MIN_AGE_DAYS — Minimum age (in days) for EIPs to be considered for release
# - EXCLUDE_TAGS — Comma-separated tag filters (e.g., DoNotDelete=*)
# - S3_BUCKET — Name of the S3 bucket to store the CSV report
# - S3_PREFIX — S3 key prefix for the report file (e.g., eip-cleanup/)
# - ONLY_WRITE_IF_CHANGES — If true, skips writing report if no EIPs were released or found

# Output:
# - CSV report in S3 with fields:
#   region, allocation_id, public_ip, domain, name_tag, age_days, in_use, excluded_by_tag, note, released, scan_timestamp, account_id
# - CloudWatch metrics:
#   CandidatesFound, Released

# Deployment Notes:
# - Recommended to trigger via EventBridge (e.g., daily or weekly).
# - Use Lambda environment variables to customize behavior without code changes.
# - Consider versioning and aliasing for safe rollbacks.


import os
import csv
import io
import json
import logging
import datetime as dt
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed

import boto3
from botocore.config import Config
from dotenv import load_dotenv
from utility.devops_library import setup_safe_logging

# ---------------- Load Environment ----------------
load_dotenv()

# ---------------- Logging Setup ----------------
log_path = setup_safe_logging("aws_ElasticIp_Cleanup_Optimization.log")
logging.info("Log setup complete. Using file: %s", log_path)

logger.setLevel(logging.INFO)

# ---------------- Configurations ----------------
CONFIG = Config(retries={"max_attempts": 10, "mode": "standard"})

# Environment variables
REGIONS = [r.strip() for r in os.getenv("REGIONS", "").split(",") if r.strip()]
APPLY = os.getenv("APPLY", "false").lower() == "true"
MIN_AGE_DAYS = int(os.getenv("MIN_AGE_DAYS", "2"))
EXCLUDE_TAGS = os.getenv("EXCLUDE_TAGS", "DoNotDelete=*")
S3_BUCKET = os.getenv("S3_BUCKET", "")
S3_PREFIX = os.getenv("S3_PREFIX", "eip-cleanup/")
ONLY_WRITE_IF_CHANGES = os.getenv("ONLY_WRITE_IF_CHANGES", "false").lower() == "true"

# ---------------- Helpers ----------------

def parse_tag_filter(s):
    out = {}
    for token in s.split(","):
        token = token.strip()
        if "=" in token:
            k, v = token.split("=", 1)
        else:
            k, v = token, "*"
        out[k.strip()] = v.strip()
    return out

EXCLUDE_TAGS_MAP = parse_tag_filter(EXCLUDE_TAGS)

def now_utc():
    return dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)

def to_utc(d):
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)

def has_excluded_tag(tags, excludes):
    tag_map = {t["Key"]: t.get("Value", "") for t in (tags or [])}
    for k, v in excludes.items():
        if k in tag_map and (v == "*" or tag_map[k] == v):
            return True
    return False

def list_regions(session):
    if REGIONS:
        return REGIONS
    ec2 = session.client("ec2", config=CONFIG)
    resp = ec2.describe_regions(AllRegions=False)
    return [r["RegionName"] for r in resp["Regions"]]

def natgw_eip_allocation_ids(ec2):
    allocs = set()
    paginator = ec2.get_paginator("describe_nat_gateways")
    for page in paginator.paginate():
        for ngw in page.get("NatGateways", []):
            for addr in ngw.get("NatGatewayAddresses", []):
                aid = addr.get("AllocationId")
                if aid:
                    allocs.add(aid)
    return allocs

def eip_age_days(addr):
    alloc_time = addr.get("AllocationTime")
    if not alloc_time:
        return 9999
    return (now_utc() - to_utc(alloc_time)).days

def eip_in_use(addr, natgw_alloc_ids):
    if addr.get("AssociationId") or addr.get("NetworkInterfaceId"):
        return True
    if addr.get("AllocationId") in natgw_alloc_ids:
        return True
    # Placeholder: Add Global Accelerator and NLB checks here if needed
    return False

def write_csv_to_s3(s3, bucket, key, rows):
    headers = [
        "region", "allocation_id", "public_ip", "domain", "name_tag",
        "age_days", "in_use", "excluded_by_tag", "note", "released", "scan_timestamp", "account_id"
    ]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=headers)
    w.writeheader()
    w.writerows(rows)
    data = buf.getvalue().encode("utf-8")
    s3.put_object(Bucket=bucket, Key=key, Body=data, ContentType="text/csv")
    return f"s3://{bucket}/{key}"

def push_metric(cloudwatch, name, value):
    cloudwatch.put_metric_data(
        Namespace="EIPCleanup",
        MetricData=[{
            "MetricName": name,
            "Value": value,
            "Unit": "Count"
        }]
    )

# ---------------- Region Processing ----------------

def process_region(region, session, apply, min_age_days, excludes, account_id, timestamp):
    ec2 = session.client("ec2", region_name=region, config=CONFIG)
    natgw_alloc_ids = natgw_eip_allocation_ids(ec2)
    rows, found, released = [], 0, 0

    paginator = ec2.get_paginator("describe_addresses")
    for page in paginator.paginate():
        for addr in page.get("Addresses", []):
            allocation_id = addr.get("AllocationId")
            public_ip = addr.get("PublicIp")
            domain = addr.get("Domain", "vpc")
            tags = addr.get("Tags", [])
            name_tag = next((t["Value"] for t in tags if t["Key"] == "Name"), "")
            age = eip_age_days(addr)
            in_use = eip_in_use(addr, natgw_alloc_ids)
            excluded = has_excluded_tag(tags, excludes)

            note = ""
            released_flag = "no"

            if not in_use and age >= min_age_days and not excluded:
                found += 1
                if apply:
                    try:
                        if allocation_id:
                            ec2.release_address(AllocationId=allocation_id)
                        else:
                            ec2.release_address(PublicIp=public_ip)
                        released_flag = "yes"
                        released += 1
                        note = "Released"
                    except ClientError as e:
                        note = f"Release failed: {e.response.get('Error', {}).get('Message', str(e))}"
                        logger.error(traceback.format_exc())
                else:
                    note = "Dry-run: would release"
            else:
                if in_use:
                    note = "In use"
                elif excluded:
                    note = "Excluded by tag"
                elif age < min_age_days:
                    note = f"Too new (< {min_age_days}d)"
                else:
                    note = "Skipped"

            rows.append({
                "region": region,
                "allocation_id": allocation_id or "",
                "public_ip": public_ip or "",
                "domain": domain,
                "name_tag": name_tag,
                "age_days": age,
                "in_use": str(in_use).lower(),
                "excluded_by_tag": str(excluded).lower(),
                "note": note,
                "released": released_flag,
                "scan_timestamp": timestamp,
                "account_id": account_id
            })

    return rows, found, released

# ---------------- Lambda Handler ----------------

def lambda_handler(event, context):
    session = boto3.Session()
    s3 = session.client("s3", config=CONFIG)
    sts = session.client("sts", config=CONFIG)
    cloudwatch = session.client("cloudwatch", config=CONFIG)
    account_id = sts.get_caller_identity()["Account"]

    regions = list_regions(session)
    timestamp = dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    s3_key = f"{S3_PREFIX.rstrip('/')}/eip_cleanup_{account_id}_{timestamp}.csv"

    all_rows, total_found, total_released = [], 0, 0

    with ThreadPoolExecutor(max_workers=min(10, len(regions))) as executor:
        futures = {
            executor.submit(process_region, region, session, APPLY, MIN_AGE_DAYS, EXCLUDE_TAGS_MAP, account_id, timestamp): region
            for region in regions
        }
        for future in as_completed(futures):
            if context.get_remaining_time_in_millis() < 10000:
                logger.warning("Approaching Lambda timeout, exiting early.")
                break
            try:
                rows, found, released = future.result()
                all_rows.extend(rows)
                total_found += found
                total_released += released
            except Exception as e:
                logger.error(f"Error processing region {futures[future]}: {e}")
                logger.debug(traceback.format_exc())

    if ONLY_WRITE_IF_CHANGES and total_found == 0 and total_released == 0:
        return {
            "status": "ok",
            "message": "no unused EIPs found",
            "regions": regions,
            "apply": APPLY,
            "min_age_days": MIN_AGE_DAYS
        }

    uri = None
    if S3_BUCKET:
        uri = write_csv_to_s3(s3, S3_BUCKET, s3_key, all_rows)

    push_metric(cloudwatch, "CandidatesFound", total_found)
    push_metric(cloudwatch, "Released", total_released)

# ---------------- Execution ----------------
 # lambda invokations