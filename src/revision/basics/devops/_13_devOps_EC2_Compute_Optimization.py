# Use Case: Cloud Cost Optimization — EC2 Rightsizing Using Compute Optimizer and handle concurrency, CloudWatch, and VPC.

# Overview:
# This AWS Lambda function runs on a schedule (EventBridge) and drops a timestamped CSV report in S3.
# It uses Compute Optimizer to identify EC2 instances for rightsizing and can optionally apply changes (stop/modify/start).
# Key features:
# 1. Controlled entirely by environment variables (no CLI args).
# 2. Writes a timestamped CSV to S3 with findings and actions.
# 3. Skips Auto Scaling instances, supports tag filters, and uses a performance‑risk guardrail.
# 4. Operates across multiple AWS regions.
# 5. Sends Slack notifications on completion or failure.
# 6. Includes timeout guard to prevent long-running executions.
# 7. Supports dry-run mode for safe testing.

# IAM Permissions Required (Lambda Execution Role):
# Ensure the Lambda role includes the following permissions:
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     { "Effect": "Allow", "Action": ["sts:GetCallerIdentity"], "Resource": "*" },
#     {
#       "Effect": "Allow",
#       "Action": [
#         "ec2:DescribeInstances",
#         "ec2:DescribeRegions",
#         "ec2:CreateTags",
#         "ec2:StopInstances",
#         "ec2:StartInstances",
#         "ec2:ModifyInstanceAttribute"
#       ],
#       "Resource": "*"
#     },
#     {
#       "Effect": "Allow",
#       "Action": ["compute-optimizer:GetEC2InstanceRecommendations"],
#       "Resource": "*"
#     },
#     {
#       "Effect": "Allow",
#       "Action": ["s3:PutObject"],
#       "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
#     }
#   ]
# }

# Environment Variables:
# SLACK_WEBHOOK           # Slack webhook URL for notifications
# DRY_RUN                 # "true" to simulate actions without applying changes
# TIMEOUT                 # Max execution time in seconds (e.g., 300)
# REGIONS                 # Comma-separated list of AWS regions to scan (optional)
# INCLUDE_TAGS            # Tags to include (e.g., "Environment=Prod,Owner=*,App=Payments")
# EXCLUDE_TAGS            # Tags to exclude (e.g., "DoNotRightsize=*,Tier=Critical")
# PERFORMANCE_RISK_MAX    # Max acceptable performance risk (e.g., 0.5)
# APPLY                   # "true" to apply recommended instance type changes
# RECOMMENDATION_RANK     # Rank of recommendation to apply (e.g., 1 for best)
# S3_BUCKET               # Target S3 bucket for report
# S3_PREFIX               # Folder path within the bucket (e.g., "ec2-rightsizing/")
# ONLY_WRITE_IF_FINDINGS # "true" to skip writing report if no recommendations found

# Output:
# - A CSV file is written to S3 with the following fields:
#   account_id, region, instance_id, name_tag,
#   current_type, platform, finding,
#   recommended_type, recommendation_rank, performance_risk,
#   applied, note

# Notifications:
# - Slack messages are sent on:
#   - Successful completion with summary
#   - Errors or exceptions during execution

# Notes:
# - Uses boto3 and botocore with retry config
# - Handles concurrency and timeout gracefully
# - Designed for safe automation with dry-run and tag filtering

import os
import csv
import io
import json
import logging
import aiohttp
import boto3
from datetime import datetime, timezone, timedelta
from botocore.config import Config
from botocore.exceptions import ClientError
from utility.devops_library import setup_safe_logging
from dotenv import load_dotenv

# ---------------- Load Environment ----------------
load_dotenv()

# ---------------- Logging Setup ----------------
log_path = setup_safe_logging("aws_EC2_Compute_Optimization.log")
logging.info("Log setup complete. Using file: %s", log_path)

# ---------------- Configuration ----------------
CONFIG = Config(retries={"max_attempts": 10, "mode": "standard"})

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "300"))

REGIONS = [r.strip() for r in os.getenv("REGIONS", "").split(",") if r.strip()]
INCLUDE_TAGS = os.getenv("INCLUDE_TAGS", "")
EXCLUDE_TAGS = os.getenv("EXCLUDE_TAGS", "")
PERFORMANCE_RISK_MAX = float(os.getenv("PERFORMANCE_RISK_MAX", "0.5"))
APPLY = os.getenv("APPLY", "false").lower() == "true"
RECOMMENDATION_RANK = int(os.getenv("RECOMMENDATION_RANK", "1"))
S3_BUCKET = os.getenv("S3_BUCKET", "")
S3_PREFIX = os.getenv("S3_PREFIX", "ec2-rightsizing/")
ONLY_WRITE_IF_FINDINGS = os.getenv("ONLY_WRITE_IF_FINDINGS", "false").lower() == "true"

# ---------------- Validation ----------------
if not SLACK_WEBHOOK or not SLACK_WEBHOOK.startswith("https://hooks.slack.com/"):
    raise ValueError("Missing or invalid SLACK_WEBHOOK configuration")

# ---------------- Slack Notification ----------------
async def send_slack_message(message):
    if DRY_RUN:
        logging.info(f"[DRY RUN] Slack message: {message}")
        return
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(SLACK_WEBHOOK, json={"text": message}) as resp:
                if resp.status != 200:
                    logging.error(f"Slack notification failed: {await resp.text()}")
    except Exception as e:
        logging.warning(f"Slack send error: {e}")

# ---------------- Helper Functions ----------------
def parse_tag_kv_list(s):
    out = {}
    s = s.strip()
    if not s:
        return out
    for token in s.split(","):
        token = token.strip()
        if not token:
            continue
        try:
            k, v = token.split("=", 1) if "=" in token else (token, "*")
            out[k.strip()] = v.strip()
        except ValueError:
            logging.warning(f"Invalid tag format: {token}")
    return out

INCLUDE_TAGS_MAP = parse_tag_kv_list(INCLUDE_TAGS)
EXCLUDE_TAGS_MAP = parse_tag_kv_list(EXCLUDE_TAGS)

def log(event, **kw):
    rec = {"msg": event, **kw}
    logging.info(json.dumps(rec, default=str))

def list_regions(session):
    if REGIONS:
        return REGIONS
    ec2 = session.client("ec2", config=CONFIG)
    resp = ec2.describe_regions(AllRegions=False)
    return [r["RegionName"] for r in resp["Regions"]]

def is_in_asg(instance):
    for t in instance.get("Tags", []):
        if t["Key"] in ("aws:autoscaling:groupName", "aws:autoscaling:groupId"):
            return True
    return False

def has_required_tags(instance, include_tags, exclude_tags):
    tags = {t["Key"]: t["Value"] for t in instance.get("Tags", [])}
    for k, v in include_tags.items():
        if k not in tags or (v != "*" and tags[k] != v):
            return False
    for k, v in exclude_tags.items():
        if k in tags and (v == "*" or tags[k] == v):
            return False
    return True

def get_instances(session, region, include_tags, exclude_tags):
    ec2 = session.client("ec2", region_name=region, config=CONFIG)
    paginator = ec2.get_paginator("describe_instances")
    for page in paginator.paginate():
        for r in page.get("Reservations", []):
            for i in r.get("Instances", []):
                if i["State"]["Name"] not in ("running", "stopped"):
                    continue
                if is_in_asg(i):
                    continue
                if not has_required_tags(i, include_tags, exclude_tags):
                    continue
                yield i

def instance_arn(account_id, region, instance_id):
    return f"arn:aws:ec2:{region}:{account_id}:instance/{instance_id}"

def get_compute_optimizer_recos(session, region, instance_arns):
    co = session.client("compute-optimizer", region_name=region, config=CONFIG)
    recos = []
    next_token = None
    while True:
        kwargs = {"instanceArns": instance_arns}
        if next_token:
            kwargs["nextToken"] = next_token
        resp = co.get_ec2_instance_recommendations(**kwargs)
        recos.extend(resp.get("instanceRecommendations", []))
        next_token = resp.get("nextToken")
        if not next_token:
            break
    return recos

def stop_modify_start(ec2, instance_id, new_type, dry_run=True):
    desc = ec2.describe_instances(InstanceIds=[instance_id])
    state = desc["Reservations"][0]["Instances"][0]["State"]["Name"]
    if state == "running":
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=dry_run)
        if not dry_run:
            ec2.get_waiter("instance_stopped").wait(InstanceIds=[instance_id])
    ec2.modify_instance_attribute(InstanceId=instance_id, InstanceType={"Value": new_type}, DryRun=dry_run)
    if state == "running":
        ec2.start_instances(InstanceIds=[instance_id], DryRun=dry_run)

def write_csv_to_s3(s3, bucket, key, rows):
    if not bucket:
        log("S3_BUCKET not set; skipping write")
        return None
    fieldnames = [
        "account_id", "region", "instance_id", "name_tag",
        "current_type", "platform", "finding",
        "recommended_type", "recommendation_rank", "performance_risk",
        "applied", "note"
    ]
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    data = buf.getvalue().encode("utf-8")
    s3.put_object(Bucket=bucket, Key=key, Body=data, ContentType="text/csv")
    return f"s3://{bucket}/{key}"

# ---------------- Lambda Handler/Core Logic ----------------
async def lambda_handler(event, context):
    start_time = datetime.now(timezone.utc)
    def is_timed_out():
        return (datetime.now(timezone.utc) - start_time).total_seconds() > TIMEOUT

    try:
        session = boto3.Session()
        sts = session.client("sts")
        account_id = sts.get_caller_identity()["Account"]
        regions = list_regions(session)

        rows = []
        total_applied = 0
        total_candidates = 0

        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        s3_key = f"{S3_PREFIX.rstrip('/')}/ec2_rightsizing_{timestamp}.csv"
        s3 = session.client("s3", config=CONFIG)

        for region in regions:
            if is_timed_out():
                raise TimeoutError("Lambda execution timed out")

            ec2 = session.client("ec2", region_name=region, config=CONFIG)
            instances = list(get_instances(session, region, INCLUDE_TAGS_MAP, EXCLUDE_TAGS_MAP))
            if not instances:
                continue

            inst_by_id = {i["InstanceId"]: i for i in instances}
            arns = [instance_arn(account_id, region, iid) for iid in inst_by_id]
            recos_all = []
            for i in range(0, len(arns), 400):
                recos_all.extend(get_compute_optimizer_recos(session, region, arns[i:i+400]))

            rec_map = {r["instanceArn"].split("/")[-1]: r for r in recos_all if "instanceArn" in r}

            for iid, inst in inst_by_id.items():
                name_tag = next((t["Value"] for t in inst.get("Tags", []) if t["Key"] == "Name"), "")
                platform = inst.get("PlatformDetails", "Linux/UNIX")
                current_type = inst["InstanceType"]
                reco = rec_map.get(iid)

                if not
# ---------------- Execution ----------------
 # lambda invokations