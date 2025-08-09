# Use Case: Cloud Cost Optimization — Identifying Stale EBS Snapshots in AWS

# Overview:
# This AWS Lambda function helps reduce cloud storage costs by identifying and deleting stale EBS snapshots.
# It performs the following steps:
# 
# 1. Fetches all EBS snapshots owned by the account (using 'OwnerIds=["self"]').
# 2. Retrieves a list of active EC2 instances (states: 'running' and 'stopped').
# 3. For each snapshot:
#    - Checks if it's older than 30 days.
#    - Skips deletion if it has a tag matching the preserve filter (e.g., "Preserve": "true").
#    - If associated with a volume, checks whether that volume is attached to any active instance.
#    - If not associated or attached to inactive resources, marks it as stale.
# 4. Deletes stale snapshots (unless DRY_RUN is enabled).
# 5. Sends a Slack notification summarizing the cleanup.

# Sample Tag Filter:
# Snapshots with specific tags (e.g., "Preserve": "true") are excluded from deletion.

# Sample Age Filter:
# Only snapshots older than 30 days are considered for deletion.

# Notification:
# Slack alerts are sent after cleanup, or on errors (if configured).

# IAM Permissions Required (Lambda Execution Role):
# Ensure the Lambda role includes the following permissions:
# {
#     "Effect": "Allow",
#     "Action": [
#         "ec2:DescribeSnapshots",
#         "ec2:DescribeVolumes",
#         "ec2:DescribeInstances",
#         "ec2:DeleteSnapshot"
#     ],
#     "Resource": "*"
# }

# Optional Environment Variables:
# - AWS_REGIONS: Comma-separated list of regions to scan (e.g., "us-east-1,us-west-2")
# - DRY_RUN: If "true", no snapshots are deleted (safe mode)
# - SLACK_WEBHOOK: Slack Incoming Webhook URL for notifications
# - PRESERVE_TAGS: Comma-separated tag filters (e.g., "Preserve:true,Environment:Production")



import boto3
import os
import logging
import asyncio
import aiohttp
from botocore.exceptions import ClientError, NoCredentialsError


from datetime import datetime, timezone, timedelta
from utility.devops_library import setup_safe_logging
from dotenv import load_dotenv

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------

# Set up logging
log_path = setup_safe_logging("aws_EBS_Cloud_Cost_Optimization.log")

# Log something
logging.info("Log setup complete. Using file: %s", log_path)

# ---------------- Configuration ----------------
AWS_REGIONS = os.getenv("AWS_REGIONS", "us-east-1").split(",")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "300"))

# ---------------- Validation ----------------
# Validate required config
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
           
def delete_snapshot(ec2_client, snapshot_id, reason):
    ec2_client.delete_snapshot(SnapshotId=snapshot_id)
    print(f"Deleted snapshot {snapshot_id}: {reason}")

def get_active_instance_ids(ec2):
    paginator = ec2.get_paginator('describe_instances')
    active_ids = set()
    for page in paginator.paginate(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}]):
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                active_ids.add(instance['InstanceId'])
    return active_ids

def get_all_snapshots(ec2):
    paginator = ec2.get_paginator('describe_snapshots')
    for page in paginator.paginate(OwnerIds=['self']):
        for snapshot in page['Snapshots']:
            yield snapshot

def is_snapshot_old(snapshot, days=30):
    created = snapshot['StartTime']
    age = datetime.now(timezone.utc) - created
    return age > timedelta(days=days)

def should_preserve_snapshot(snapshot, preserve_tags={"Preserve": "true"}):
    # Normalize Tag Keys and Values
    tags = {
        tag['Key'].strip().lower(): tag['Value'].strip().lower()
        for tag in snapshot.get('Tags', [])
    }
    for key, value in preserve_tags.items():
        if tags.get(key.strip().lower()) == value.strip().lower():
            return True
    return False

def parse_preserve_tags():
    raw = os.getenv("PRESERVE_TAGS", "")
    tag_pairs = []
    for pair in raw.split(","):
        if ":" in pair:
            k, v = pair.split(":", 1)
            tag_pairs.append((k.strip(), v.strip()))
        else:
            logging.warning(f"Invalid tag format skipped: {pair}")
    return {k: v for k, v in tag_pairs}

# ---------------- Lambda Handler/Core Logic ----------------

def lambda_handler(event, context):
    for region in AWS_REGIONS:
        try:
            ec2 = boto3.client('ec2', region_name=region)

            # Get all running EC2 instance IDs
            active_instance_ids = get_active_instance_ids(ec2)
            stale_snapshots = []

            # Iterate through all snapshots using pagination
            for snapshot in get_all_snapshots(ec2):
                snapshot_id = snapshot['SnapshotId']
                volume_id = snapshot.get('VolumeId')

                # Only delete snapshots older than 30 days.
                if not is_snapshot_old(snapshot):
                    logging.info(f"Skipping snapshot {snapshot_id}: not older than 30 days")
                    continue

                # Preserve snapshots with specific tags (matched
                if should_preserve_snapshot(snapshot, preserve_tags):
                    logging.info(f"Preserving snapshot {snapshot_id}: matched preserve tags")
                    continue

                # Only delete snapshots not attached to any volume.
                if not volume_id:
                    stale_snapshots.append((snapshot_id, "not attached to any volume"))
                    continue

                try:
                    volume = ec2.describe_volumes(VolumeIds=[volume_id])['Volumes'][0]
                    attachments = volume.get('Attachments', [])
                    attached_instance_ids = {
                        att['InstanceId'] for att in attachments if 'InstanceId' in att
                    }

                    if not attached_instance_ids & active_instance_ids:
                        stale_snapshots.append((snapshot_id, "volume not attached to any active instance"))

                except ClientError as e:
                    if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                        stale_snapshots.append((snapshot_id, "associated volume not found"))

            for snapshot_id, reason in stale_snapshots:
                if DRY_RUN:
                    logging.info(f"[DRY RUN] Would delete snapshot {snapshot_id}: {reason}")
                else:
                    try:
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        logging.info(f"Deleted snapshot {snapshot_id}: {reason}")
                    except ClientError as e:
                        logging.error(f"Failed to delete snapshot {snapshot_id}: {e}")

            if stale_snapshots:
                asyncio.run(send_slack_message(
                    f":wastebasket: Deleted {len(stale_snapshots)} stale EBS snapshots in {region}"
                ))

        except NoCredentialsError:
            logging.critical(f"Missing AWS credentials for region {region}")
            asyncio.run(send_slack_message(f":warning: Missing AWS credentials for {region}"))
        except Exception as e:
            logging.critical(f"Snapshot cleanup failed in {region}: {e}")

# ---------------- Execution ----------------
 # lambda invokations