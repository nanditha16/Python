# Use Case: Waiting for Pods to Become Ready :
# After deploying an application to a Kubernetes cluster,
# you want to wait until all pods are ready before proceeding 
# (for example, before running smoke tests or promoting to production).
# Using a while loop lets you keep checking until a success/failure condition is reached.

## Uses official Kubernetes Python client (no kubectl) to fetch pod readiness statu.
## Loops until all pods are ready or a timeout is reached.
## Logs progress every 10 seconds.
## Raises an exception if pods are not ready within the given timeout.
## Monitors multiple deployments in parallel.
## Adds Slack notification on timeout or success.
## Includes retry logic if API calls fail.

import subprocess
import time
import logging
import os
import requests

import asyncio
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import aiohttp

from utility.devops_library import setup_safe_logging
from dotenv import load_dotenv

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------

# Set up logging
log_path = setup_safe_logging("pod_deploy_readiness_logging.log")

# Log something
logging.info("Log setup complete. Using file: %s", log_path)

# ---------------- Configuration ----------------

DEPLOYMENTS = [
    {"name": os.getenv("DEPLOYMENT_1", "my-app"), "namespace": os.getenv("NAMESPACE_1", "default")},
    {"name": os.getenv("DEPLOYMENT_2", "my-worker"), "namespace": os.getenv("NAMESPACE_2", "default")}
]

TIMEOUT = int(os.getenv("TIMEOUT", "300")) # seconds
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "10")) # seconds
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

MAX_RETRIES = 5
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

# Validate required config
if not SLACK_WEBHOOK or not SLACK_WEBHOOK.startswith("https://hooks.slack.com/"):
    raise ValueError("Invalid or missing SLACK_WEBHOOK")

for dep in DEPLOYMENTS:
    if not dep["name"] or not dep["namespace"]:
        raise ValueError(f"Deployment config invalid: {dep}")
        
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

# ---------------- Kubernetes Setup ----------------
def init_k8s_client():
    try:
        config.load_incluster_config()
        logging.info("Loaded in-cluster Kubernetes config")
    except config.ConfigException:
        try:
            config.load_kube_config()
            logging.info("Loaded local kube config")
        except config.ConfigException as e:
            msg = "Kubernetes config not found. Ensure you're running in a cluster or have a valid kubeconfig."
            logging.error(msg)
            raise RuntimeError(msg) from e

apps_v1 = client.AppsV1Api()
# ---------------- Core Logic ----------------
# ---------------- Pod Readiness Check ----------------
# Pod Readiness Check
async def get_ready_pod_count(name, namespace):
    for attempt in range(MAX_RETRIES):
        try:
            dep = apps_v1.read_namespaced_deployment(name, namespace)
            ready = dep.status.ready_replicas or 0
            total = dep.status.replicas or 0
            return ready, total
        except ApiException as e:
            logging.error(f"K8s API error fetching {name}: {e}")
            if attempt < MAX_RETRIES - 1:
                await asyncio.sleep(2 ** attempt)  # exponential backoff
            else:
                return None, None

# ---------------- Wait for Deployment ----------------

# Wait for Pods
async def wait_for_deployment_ready(name, namespace):
    start_time = time.time()
    while True:
        ready, total = await get_ready_pod_count(name, namespace)

        if ready is None and total is None:
            msg = f"Max retries reached for deployment {name} in {namespace}."
            logging.error(msg)
            await send_slack_message(f":x: {msg}")
            return False

        logging.info(f"Deployment {name}: {ready}/{total} pods ready.")

        if total > 0 and ready == total:
            msg = f"Deployment {name} in {namespace} is ready: {ready}/{total} pods."
            logging.info(msg)
            await send_slack_message(msg)
            return True

        if time.time() - start_time > TIMEOUT:
            msg = f"Timeout: Deployment {name} in {namespace} not ready after {TIMEOUT} seconds."
            logging.error(msg)
            await send_slack_message(msg)
            return False

        await asyncio.sleep(CHECK_INTERVAL)

# ---------------- Safe Task Wrapper ----------------
async def safe_task(task):
    try:
        return await task
    except Exception as e:
        logging.error(f"Unhandled task error: {e}")
        await send_slack_message(f":x: Unhandled task error: {e}")
        return False
    
# ---------------- Monitor All Deployments ----------------
async def monitor_all_deployments():
    tasks = [wait_for_deployment_ready(dep["name"], dep["namespace"]) for dep in DEPLOYMENTS]
    results = await asyncio.gather(*tasks)
    if all(results):
        logging.info("All deployments are ready.")
    else:
        logging.warning("Some deployments failed to become ready in time.")

# ---------------- Execution ----------------
async def main():
    logging.info("Starting Kubernetes deployment readiness monitor...")
    try:
        init_k8s_client()
    except RuntimeError as e:
        logging.critical(f"Startup failed: {e}")
        await send_slack_message(f":warning: Startup failed: {e}")
        return  # Exit gracefully

    await monitor_all_deployments()

if __name__ == "__main__":
    asyncio.run(main())