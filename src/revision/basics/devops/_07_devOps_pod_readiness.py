# Use Case: Waiting for Pods to Become Ready :
# After deploying an application to a Kubernetes cluster,
# you want to wait until all pods are ready before proceeding 
# (for example, before running smoke tests or promoting to production).
# Using a while loop lets you keep checking until a success/failure condition is reached.

## Uses kubectl to fetch pod readiness status from Kubernetes.
## Loops until all pods are ready or a timeout is reached.
## Logs progress every 10 seconds.
## Raises an exception if pods are not ready within the given timeout.
## Adds Slack notification on timeout or success.
## Includes retry logic if API calls fail.

import subprocess
import time
import logging
import os
import requests
from utility.devops_library import setup_safe_logging
from dotenv import load_dotenv

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------

# Set up logging
log_path = setup_safe_logging("pod_deploy_readiness.log")

# Log something
logging.info("Log setup complete. Using file: %s", log_path)

# ---------------- Configuration ----------------

DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME", "my-app")
NAMESPACE = os.getenv("NAMESPACE", "default")
TIMEOUT = int(os.getenv("TIMEOUT", "300"))
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "10"))
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

MAX_RETRIES = 5

# Validate required config
if not SLACK_WEBHOOK:
    logging.error("Missing SLACK_WEBHOOK environment variable.")
    raise EnvironmentError("SLACK_WEBHOOK is required.")
    
# ---------------- Slack Notification ----------------
def notify_slack(message):
    if SLACK_WEBHOOK:
        try:
            requests.post(SLACK_WEBHOOK, json={"text": message})
        except Exception as e:
            logging.warning(f"Failed to send Slack notification: {e}")

# ---------------- Pod Readiness Check ----------------
def get_ready_pod_count():
    """Return (ready_pods, total_pods) for a deployment using kubectl."""
    try:
        cmd = [
            "kubectl", "get", "deployment", DEPLOYMENT_NAME,
            "-n", NAMESPACE, "-o",
            "jsonpath={.status.readyReplicas},{.status.replicas}"
        ]
        output = subprocess.check_output(cmd, text=True).strip()
        if output:
            ready, total = output.split(",")
            return int(ready or 0), int(total or 0)
        return 0, 0
    except subprocess.CalledProcessError as e:
        logging.error(f"Error getting deployment status: {e}")
        return None

# ---------------- Wait for Pods ----------------
def wait_for_pods_ready():
    start_time = time.time()
    retries = 0

    while True:
        result = get_ready_pod_count()

        if result is None:
            retries += 1
            logging.warning(f"Retrying... ({retries}/{MAX_RETRIES})")
            if retries >= MAX_RETRIES:
                msg = f"Max retries reached while checking pod status for {DEPLOYMENT_NAME}."
                logging.error(msg)
                notify_slack(msg)
                return
            time.sleep(CHECK_INTERVAL)
            continue

        retries = 0  # Reset on success
        ready, total = result
        logging.info(f"Deployment {DEPLOYMENT_NAME}: {ready}/{total} pods ready.")

        if total > 0 and ready == total:
            msg = f"All pods for {DEPLOYMENT_NAME} are ready!"
            logging.info(msg)
            notify_slack(msg)
            return

        if time.time() - start_time > TIMEOUT:
            msg = f"Timeout: Pods for {DEPLOYMENT_NAME} not ready after {TIMEOUT} seconds."
            logging.error(msg)
            notify_slack(msg)
            return

        time.sleep(CHECK_INTERVAL)

 # ---------------- Execution ----------------

if __name__ == "__main__":
    wait_for_pods_ready()


