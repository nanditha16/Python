# # Use Case: Monitoring and Reporting:
## In scenarios where you need to gather data or perform checks on multiple systems, a "for" loop is handy. 
## Parallel execution using asyncio + asyncssh (faster than sequential SSH) – Log monitoring runs alongside server resource monitoring.
## Runs commands: uptime, memory usage, disk usage.
## Threshold alerts: CPU & Memory threshold alerts (WARN if Memory > 80% or Disk > 90%).
## Slack notification - Sends Slack, Email, PagerDuty alerts.
## PagerDuty trigger (Events API v2).
## Push report to S3 or Azure Blob for central storage.
## Full logging + error handling - Saves a timestamped report locally.
## Log Rotation Handling – Uses file inode check to detect rotation and reopen the log file.
## Regex Patterns – Allows flexible, case-insensitive log pattern matching.

import re
import os
import time
from dotenv import load_dotenv

import logging
from datetime import datetime
from utility.devops_library import setup_safe_logging
import asyncssh
import asyncio
import aiofiles
import smtplib
from email.mime.text import MIMEText
import aiohttp
import boto3
from azure.storage.blob import BlobServiceClient

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------
# Set up logging
log_path = setup_safe_logging("server_monitoring.log")

# Log something
logging.info("Log setup complete. Using file: %s", log_path)


# ---------------- Configurations ----------------
# ---------------- Monitoring Commands and Configurations ----------------
LOG_FILES = ["pod_deploy_readinessa.log", "server_monitoring.log"]

PATTERNS = [re.compile(p, re.IGNORECASE) for p in ["Error", "ORA-*", "exception"]]
# Commands to run on each server to gather resource information
COMMANDS = {
    "uptime": "uptime",
    "memory": "free -m | grep Mem",
    "disk": "df -h /"
}
MEMORY_THRESHOLD = 80  # %
DISK_THRESHOLD = 90    # %

# Use environment variables or a secure secrets manager (e.g., AWS Secrets Manager, Azure Key Vault, HashiCorp Vault).
# Secrets
SSH_PASSWORD = os.getenv("SSH_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO", "").split(",")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
PAGERDUTY_ROUTING_KEY = os.getenv("PAGERDUTY_ROUTING_KEY")
# Azure Blob Configuration
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")
# S3 Configuration
S3_BUCKET = os.getenv("S3_BUCKET")
S3_PREFIX = os.getenv("S3_PREFIX", "")

# Validate required secrets
REQUIRED_SECRETS = {
    "SSH_PASSWORD": SSH_PASSWORD,
    "SMTP_USER": SMTP_USER,
    "SMTP_PASSWORD": SMTP_PASSWORD,
    "SLACK_WEBHOOK": SLACK_WEBHOOK,
    "PAGERDUTY_ROUTING_KEY": PAGERDUTY_ROUTING_KEY,
    "AZURE_CONNECTION_STRING": AZURE_CONNECTION_STRING,
}
missing = [key for key, val in REQUIRED_SECRETS.items() if not val]
if missing:
    logging.error(f"Missing secrets: {', '.join(missing)}")
    raise EnvironmentError("Required secrets are missing. Please set them via environment variables or a .env file.")

# ensures each log file exists before starting monitoring.
async def wait_for_file(file_path, max_retries=2, delay=2):
    """Wait until file exists or retries are exhausted."""
    retries = 0
    while not os.path.exists(file_path) and retries < max_retries:
        logging.warning(f"Log file {file_path} not found, retrying... ({retries+1}/{max_retries})")
        await asyncio.sleep(delay)
        retries += 1
    return os.path.exists(file_path)

# ---------------- Server List ----------------
# List of servers with SSH connection details
SERVERS = [
    {"host": "server1.example.com", "user": "devops", "password": SSH_PASSWORD},
    {"host": "server2.example.com", "user": "devops", "password": SSH_PASSWORD},
    {"host": "server3.example.com", "user": "devops", "password": SSH_PASSWORD},
]

# ---------------- Notification Functions ----------------
async def send_slack_message(message):
    async with aiohttp.ClientSession() as session:
        await session.post(SLACK_WEBHOOK, json={"text": message})

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = ", ".join(EMAIL_TO)
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    except Exception as e:
        logging.error(f"Email send error: {e}")

async def trigger_pagerduty_alert(message):
    async with aiohttp.ClientSession() as session:
        await session.post(
            "https://events.pagerduty.com/v2/enqueue",
            json={
                "routing_key": PAGERDUTY_ROUTING_KEY,
                "event_action": "trigger",
                "payload": {
                    "summary": message,
                    "severity": "warning",
                    "source": "server-monitoring"
                }
            },
            headers={"Content-Type": "application/json"}
        )

# ---------------- Monitoring Functions ----------------
async def run_command(host, user, password, cmd):
    try:
        async with asyncssh.connect(host, username=user, password=password) as conn:
            result = await conn.run(cmd)
            if result.stderr:
                logging.error(f"[{host}] Error: {result.stderr.strip()}")
                return f"ERROR: {result.stderr.strip()}"
            return result.stdout.strip()
    except Exception as e:
        logging.error(f"[{host}] SSH error: {e}")
        return f"ERROR: {e}"

def check_thresholds(host, memory_output, disk_output):
    alerts = []
    try:
        mem_used = int(memory_output.split()[2])
        mem_total = int(memory_output.split()[1])
        mem_percent = (mem_used / mem_total) * 100
        if mem_percent > MEMORY_THRESHOLD:
            alerts.append(f"[{host}] Memory usage high: {mem_percent:.1f}%")

        disk_percent = int(disk_output.split()[4].strip('%'))
        if disk_percent > DISK_THRESHOLD:
            alerts.append(f"[{host}] Disk usage high: {disk_percent}%")
    except Exception as e:
        logging.error(f"[{host}] Threshold check error: {e}")
    return alerts

async def monitor_server(server):
    host = server["host"]
    logging.info(f"Monitoring {host}")
    async def run(cmd): return await run_command(host, server["user"], server["password"], cmd)
    results = dict(zip(COMMANDS.keys(), await asyncio.gather(*[run(cmd) for cmd in COMMANDS.values()])))
    alerts = check_thresholds(host, results.get("memory", ""), results.get("disk", ""))
    return {"host": host, "results": results, "alerts": alerts}

async def monitor_all():
    return await asyncio.gather(*[monitor_server(s) for s in SERVERS])

async def save_report(report):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"monitoring_report_{timestamp}.txt"
    try:
        async with aiofiles.open(filename, "w") as f:
            for server in report:
                await f.write(f"Server: {server['host']}\n")
                for metric, output in server["results"].items():
                    await f.write(f"  {metric}:\n    {output}\n")
                if server["alerts"]:
                    await f.write("  ALERTS:\n    " + "\n    ".join(server["alerts"]) + "\n")
                await f.write("\n")
        logging.info(f"Report saved: {filename}")
    except Exception as e:
        logging.error(f"Error saving report: {e}")
        filename = None
    return filename

def push_report_to_cloud(filename):
    try:
        s3_client = boto3.client("s3")
        s3_key = S3_PREFIX + filename
        s3_client.upload_file(filename, S3_BUCKET, s3_key)
        logging.info(f"Uploaded to S3: s3://{S3_BUCKET}/{s3_key}")
    except Exception as e:
        logging.error(f"S3 upload failed: {e}")
    try:
        blob_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container = blob_client.get_container_client(AZURE_CONTAINER)
        container.upload_blob(name=filename, data=open(filename, "rb"), overwrite=True)
        logging.info(f"Uploaded to Azure Blob: {filename}")
    except Exception as e:
        logging.error(f"Azure upload failed: {e}")

async def notify(alerts):
    if alerts:
        message = "\n".join(alerts)
        logging.warning("Alerts triggered:\n" + message)
        await send_slack_message(message)
        send_email("Server Monitoring Alert", message)
        await trigger_pagerduty_alert(message)

# ---------------- Parallel Log Monitoring ----------------
async def monitor_single_log(file_path, stop_event):
    """Monitor a single log file and handle rotation."""
    if not await wait_for_file(file_path):
        logging.error(f"Log file {file_path} not available after retries. Skipping monitoring.")
        return

    logging.info(f"Starting log monitoring for {file_path}")
    file_inode = None
    file = None

    while not stop_event.is_set():
        try:
            st = os.stat(file_path)
            if file_inode != st.st_ino:
                if file:
                    file.close()
                file = open(file_path, "r")
                file.seek(0, os.SEEK_END)
                file_inode = st.st_ino
                logging.info(f"Log file rotated or reopened: {file_path}")
        except FileNotFoundError:
            logging.warning(f"Log file {file_path} not found, retrying...")
            await asyncio.sleep(2)
            continue

        line = file.readline()
        if not line:
            await asyncio.sleep(1)
            continue

        for pattern in PATTERNS:
            if pattern.search(line):
                alert_msg = f":rotating_light: Log Alert ({file_path}): {line.strip()}"
                logging.warning(alert_msg)
                await send_slack_message(alert_msg)
                send_email("Log Alert Detected", alert_msg)
                await trigger_pagerduty_alert(alert_msg)

    if file:
        file.close()
        logging.info(f"Stopped log monitoring for {file_path}")

async def monitor_all_logs(stop_event):
    await asyncio.gather(*[monitor_single_log(f, stop_event) for f in LOG_FILES])

# ---------------- Script Execution ----------------
async def main():
    logging.info("===== Starting Async Server Monitoring =====")
    # Step 1: Run server monitoring
    report = await monitor_all()
    alerts = [alert for server in report for alert in server["alerts"]]
    await notify(alerts)
    filename = await save_report(report)
    if filename:
        push_report_to_cloud(filename)

    # Step 2: Run log monitoring for multiple log files (30 seconds)
    stop_event = asyncio.Event()
    log_task = asyncio.create_task(monitor_all_logs(stop_event))
    logging.info("===== Monitoring logs for 30 seconds =====")
    await asyncio.sleep(30)
    stop_event.set()
    await log_task

    logging.info("===== Monitoring Completed =====")

if __name__ == "__main__":
    asyncio.run(main())