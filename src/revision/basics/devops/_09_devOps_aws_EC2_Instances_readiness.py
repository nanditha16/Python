# Use Case: Wait for Amazon EC2 Instance to Become Ready
# After launching a new EC2 instance (or scaling up by adding instances),
# you need to wait until the instance status becomes "running" and passes health checks 
# before using it.
# This is often needed in automated provisioning scripts or CI/CD pipelines.

## Launches an EC2 instance (multiple) with desired type and security group.
## Uses a while loop to check:
    ## InstanceState is "running".
    ## SystemStatus is "ok".
    ## InstanceStatus is "ok".
## Logs progress every 10 seconds until the instance is healthy or times out.
    ## Waits for all to become healthy (parallel monitoring)
## Handles AWS API errors and credential issues.
## Sends Slack notifications on success or failure

import time
import logging
import os

import asyncio
import aiohttp

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

from utility.devops_library import setup_safe_logging
from dotenv import load_dotenv

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------

# Set up logging
log_path = setup_safe_logging("aws_EC2_Instances_readiness_logging.log")

# Log something
logging.info("Log setup complete. Using file: %s", log_path)

# ---------------- Configuration ----------------

AWS_REGIONS = os.getenv("AWS_REGIONS", "us-east-1").split(",")

INSTANCE_TYPE = os.getenv("INSTANCE_TYPE")
AMI_ID = os.getenv("AMI_ID") # Example Amazon Linux 2 AMI
KEY_NAME = os.getenv("KEY_NAME")
SECURITY_GROUP = os.getenv("SECURITY_GROUP")
INSTANCE_COUNT = int(os.getenv("INSTANCE_COUNT", "1"))

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

MAX_RETRIES = 5
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

TIMEOUT = int(os.getenv("TIMEOUT", "300"))

# ---------------- Validation ----------------
# Validate required config
REQUIRED_VARS = {
    "INSTANCE_TYPE": INSTANCE_TYPE,
    "AMI_ID": AMI_ID,
    "KEY_NAME": KEY_NAME,
    "SECURITY_GROUP": SECURITY_GROUP,
    "SLACK_WEBHOOK": SLACK_WEBHOOK
}
missing = [k for k, v in REQUIRED_VARS.items() if not v]
if missing or not SLACK_WEBHOOK.startswith("https://hooks.slack.com/"):
    raise ValueError(f"Missing or invalid configuration: {', '.join(missing)}")

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

# ---------------- Core Logic ----------------

# ---------------- Launch EC2 Instances ----------------
def launch_instances(count, ec2, retries=MAX_RETRIES):
    for attempt in range(1, retries + 1):
        try:
            response = ec2.run_instances(
                ImageId=AMI_ID,
                InstanceType=INSTANCE_TYPE,
                KeyName=KEY_NAME,
                SecurityGroupIds=[SECURITY_GROUP],
                MinCount=count,
                MaxCount=count
            )
            instance_ids = [inst["InstanceId"] for inst in response["Instances"]]
            logging.info(f"Launched instances: {instance_ids}")
            tag_instances(instance_ids, ec2)
            return instance_ids
        except ClientError as e:
            logging.error(f"Attempt {attempt}: EC2 launch failed: {e}")
            time.sleep(2 ** attempt)
    raise RuntimeError("Failed to launch EC2 instances after multiple retries")

# ---------------- Tag Instances ----------------
def tag_instances(instance_ids, ec2):
    try:
        ec2.create_tags(
            Resources=instance_ids,
            Tags=[{"Key": "Environment", "Value": "Dev"}]
        )
        logging.info(f"Tagged instances {instance_ids} with Environment=Dev")
    except ClientError as e:
        logging.error(f"Failed to tag instances {instance_ids}: {e}")

# ---------------- Check Instance Status ----------------
async def wait_for_instance(instance_id, ec2):
    start_time = time.time()
    while True:
        try:
            response = ec2.describe_instance_status(InstanceIds=[instance_id])
            statuses = response.get("InstanceStatuses", [])
            if statuses:
                state = statuses[0]["InstanceState"]["Name"]
                sys_status = statuses[0]["SystemStatus"]["Status"]
                inst_status = statuses[0]["InstanceStatus"]["Status"]
                logging.info(f"Instance {instance_id} state: {state}, system: {sys_status}, instance: {inst_status}")
                if state == "running" and sys_status == "ok" and inst_status == "ok":
                    return True
            else:
                logging.info(f"Instance {instance_id} status not yet available.")
        except ClientError as e:
            logging.error(f"Error checking {instance_id} status: {e}")

        if time.time() - start_time > TIMEOUT:
            logging.error(f"Timeout waiting for {instance_id}")
            return False

        await asyncio.sleep(10)

# ---------------- Parallel Wait for All Instances ----------------
async def wait_for_all_instances(instance_ids, ec2):
    tasks = [wait_for_instance(i, ec2) for i in instance_ids]
    results = await asyncio.gather(*tasks)
    failed = [i for i, r in zip(instance_ids, results) if not r]
    if failed:
        msg = f":x: Instances failed to become ready: {failed}"
        logging.error(msg)
        await send_slack_message(msg)
    else:
        msg = f":white_check_mark: All instances are running and healthy: {instance_ids}"
        logging.info(msg)
        await send_slack_message(msg)

# ---------------- Execution ----------------
async def main():
    logging.info("Starting EC2 provisioning and readiness check...")
    for region in AWS_REGIONS:
        try:
            ec2 = boto3.client("ec2", region_name=region)
            instance_ids = launch_instances(INSTANCE_COUNT, ec2)
            await wait_for_all_instances(instance_ids, ec2)
        except NoCredentialsError:
            logging.critical(f"Missing AWS credentials for region {region}")
            await send_slack_message(f":warning: Missing AWS credentials for {region}")
        except Exception as e:
            logging.critical(f"Provisioning failed in {region}: {e}")
            await send_slack_message(f":warning: EC2 provisioning failed in {region}: {e}")

if __name__ == "__main__":
    asyncio.run(main())