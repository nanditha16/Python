# Use case: Multi-Cloud VM Management
# When working with cloud infrastructure, DevOps engineers can use "for" loops to manage resources
#  like virtual machines, databases, and storage across different cloud providers.
# start/stop instances across AWS, Azure, and GCP.
## AWS: Loops through regions and starts/stops EC2 instances.
## Azure: Loops through resource group VMs and deallocates/starts them.
## GCP: Lists instances across zones and stops/starts them.
# Handle errors gracefully (wrong region, network errors, invalid credentials).
## Logs all actions and errors to cloud_resource_management.log.
## Log all actions and store an audit report.

# Add asyncio for parallel execution (faster when managing multiple accounts).
# Add tag-based filtering (e.g., only stop non-production instances).
# Send Slack or email notifications about resource changes.
# Push action audit report to S3 or Azure Blob for compliance.
import os
from dotenv import load_dotenv

import logging
from datetime import datetime
from utility.devops_library import setup_safe_logging

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------

# Set up logging
log_path = setup_safe_logging("cloud_resource_management.log")

# Log something
logging.info("Log setup complete. Using file: %s", log_path)

# ---------------- AWS SDK ----------------
try:
    import boto3
except ImportError:
    boto3 = None
    logging.warning("boto3 not installed. Skipping AWS resource management.")

# ---------------- Azure SDK ----------------
try:
    from azure.identity import DefaultAzureCredential, AzureCliCredential
    from azure.mgmt.compute import ComputeManagementClient
except ImportError:
    DefaultAzureCredential = None
    AzureCliCredential = None
    ComputeManagementClient = None
    logging.warning("Azure SDK not installed. Skipping Azure resource management.")

# ---------------- GCP SDK ----------------
try:
    from googleapiclient import discovery
    from google.oauth2 import service_account
except ImportError:
    discovery = None
    service_account = None
    logging.warning("Google API client not installed. Skipping GCP resource management.")

# ---------------- Configuration ----------------
CONFIG = {
    "AWS_REGIONS": os.getenv("AWS_REGIONS", "us-east-1,us-west-2").split(","),
    "AWS_ACTION": os.getenv("AWS_ACTION"),
    "AZURE_SUBSCRIPTION_ID": os.getenv("AZURE_SUBSCRIPTION_ID"),
    "AZURE_RESOURCE_GROUP": os.getenv("AZURE_RESOURCE_GROUP"),
    "AZURE_ACTION": os.getenv("AZURE_ACTION"),
    "GCP_PROJECT_ID": os.getenv("GCP_PROJECT_ID"),
    "GCP_ACTION": os.getenv("GCP_ACTION"),
    "SERVICE_ACCOUNT_FILE": os.getenv("SERVICE_ACCOUNT_FILE"),
}

REQUIRED_KEYS = ["AWS_ACTION", "AZURE_SUBSCRIPTION_ID", "AZURE_RESOURCE_GROUP", "AZURE_ACTION", "GCP_PROJECT_ID", "GCP_ACTION", "SERVICE_ACCOUNT_FILE"]
missing = [key for key in REQUIRED_KEYS if not CONFIG.get(key)]
if missing:
    logging.error(f"Missing required configuration: {', '.join(missing)}")
    raise EnvironmentError("Missing required environment variables. Please check your .env file or environment.")

# ---------------- AWS Function ----------------
def manage_aws_instances(action):
    if not boto3:
        logging.warning("Skipping AWS: boto3 not available.")
        return
    for region in CONFIG["AWS_REGIONS"]:
        try:
            ec2 = boto3.client("ec2", region_name=region)
            instances = ec2.describe_instances(
                Filters=[{"Name": "instance-state-name", "Values": ["running" if action == "stop" else "stopped"]}]
            )
            instance_ids = [
                i["InstanceId"]
                for r in instances["Reservations"]
                for i in r["Instances"]
            ]
            if instance_ids:
                if action == "stop":
                    ec2.stop_instances(InstanceIds=instance_ids)
                else:
                    ec2.start_instances(InstanceIds=instance_ids)
                logging.info(f"AWS ({region}): {action} {len(instance_ids)} instance(s): {instance_ids}")
            else:
                logging.info(f"AWS ({region}): No instances to {action}.")
        except Exception as e:
            logging.error(f"AWS ({region}) {action} failed: {e}")

# ---------------- Azure Function ----------------
def get_azure_compute_client(subscription_id):
    """Try DefaultAzureCredential first, fallback to AzureCliCredential if env creds not set."""
    if not ComputeManagementClient:
        logging.warning("Skipping Azure: SDK not available.")
        return None
    try:
        try:
            credential = DefaultAzureCredential(exclude_environment_credential=True)
            logging.info("Azure: Using DefaultAzureCredential")
        except Exception:
            credential = AzureCliCredential()
            logging.info("Azure: Using AzureCliCredential as fallback")
        return ComputeManagementClient(credential, subscription_id)
    except Exception as e:
        logging.error(f"Azure authentication failed: {e}")
        return None

def manage_azure_vms(action):
    compute_client = get_azure_compute_client(CONFIG["AZURE_SUBSCRIPTION_ID"])
    if not compute_client:
        logging.warning("Skipping Azure VM management due to credential error.")
        return
    try:
        vm_list = compute_client.virtual_machines.list(CONFIG["AZURE_RESOURCE_GROUP"])
        for vm in vm_list:
            vm_name = vm.name
            if action == "deallocate":
                poller = compute_client.virtual_machines.begin_deallocate(CONFIG["AZURE_RESOURCE_GROUP"], vm_name)
            else:
                poller = compute_client.virtual_machines.begin_start(CONFIG["AZURE_RESOURCE_GROUP"], vm_name)
            poller.wait()
            logging.info(f"Azure: {action} VM {vm_name}")
    except Exception as e:
        logging.error(f"Azure {action} failed: {e}")

# ---------------- GCP Function ----------------
def manage_gcp_instances(action):
    if not discovery or not service_account:
        logging.warning("Skipping GCP: SDK not available.")
        return
    try:
        credentials = service_account.Credentials.from_service_account_file(CONFIG["SERVICE_ACCOUNT_FILE"])
        service = discovery.build("compute", "v1", credentials=credentials)
        request = service.instances().aggregatedList(project=CONFIG["GCP_PROJECT_ID"])
        while request is not None:
            response = request.execute()
            for zone, instances_scoped_list in response.get("items", {}).items():
                instances = instances_scoped_list.get("instances", [])
                for instance in instances:
                    instance_name = instance["name"]
                    zone_name = instance["zone"].split("/")[-1]
                    if (action == "stop" and instance["status"] == "RUNNING") or \
                       (action == "start" and instance["status"] == "TERMINATED"):
                        if action == "stop":
                            service.instances().stop(project=CONFIG["GCP_PROJECT_ID"], zone=zone_name, instance=instance_name).execute()
                        else:
                            service.instances().start(project=CONFIG["GCP_PROJECT_ID"], zone=zone_name, instance=instance_name).execute()
                        logging.info(f"GCP: {action} VM {instance_name} in {zone_name}")
            request = service.instances().aggregatedList_next(previous_request=request, previous_response=response)
    except Exception as e:
        logging.error(f"GCP {action} failed: {e}")

# ---------------- Execution ----------------
def main():
    logging.info("===== Starting Multi-Cloud Resource Management =====")
    manage_aws_instances(CONFIG["AWS_ACTION"])
    manage_azure_vms(CONFIG["AZURE_ACTION"])
    manage_gcp_instances(CONFIG["GCP_ACTION"])
    logging.info("===== Cloud Resource Management Completed =====")

if __name__ == "__main__":
    main()