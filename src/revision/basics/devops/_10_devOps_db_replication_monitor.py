"""
Use Case: Database Replication and Data Synchronization
-------------------------------------------------------
DevOps engineers often monitor database replication to ensure data consistency.
This script uses a while loop to:
1. Connect to multiple database replicas.
2. Monitor replication lag.
3. Trigger Slack & Email alerts when lag exceeds a threshold.
4. Retry failed connections.
5. Stop after fixed monitoring duration.
"""

import os
import time
import logging
import asyncio
import aiohttp
import smtplib
from email.mime.text import MIMEText
import mysql.connector
import psycopg2
from dotenv import load_dotenv
from utility.devops_library import setup_safe_logging

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------

# Set up logging
log_path = setup_safe_logging("db_replication_monitor.log")

# ---------------- Configuration ----------------
# ---------------- Threshold & Monitoring Duration ----------------
REPLICATION_LAG_THRESHOLD = int(os.getenv("REPLICATION_LAG_THRESHOLD", "10"))  # seconds
MONITOR_DURATION = int(os.getenv("MONITOR_DURATION", "60"))  # seconds
MAX_DB_FAILURES = int(os.getenv("MAX_DB_FAILURES", "3"))

# ---------------- Notifications ----------------
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO", "").split(",")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "12"))  # e.g., 12 iterations at 5s = 1 minute
# ---------------- Database Configurations ----------------

DATABASES = [
    {
        "type": "mysql",
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DB", "")
    },
    {
        "type": "postgresql",
        "host": os.getenv("PG_HOST", "127.0.0.1"),
        "port": int(os.getenv("PG_PORT", "5432")),
        "user": os.getenv("PG_USER", "postgres"),
        "password": os.getenv("PG_PASSWORD", ""),
        "database": os.getenv("PG_DB", "")
    }
]

DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

# ---------------- Validation ----------------
if not (SLACK_WEBHOOK and SLACK_WEBHOOK.startswith("https://hooks.slack.com/")):
    raise ValueError("Invalid Slack Webhook URL")

REQUIRED_VARS = {
    "EMAIL_FROM": EMAIL_FROM,
    "EMAIL_TO": EMAIL_TO,
    "SMTP_USER": SMTP_USER,
    "SMTP_PASSWORD": SMTP_PASSWORD
}
missing = [k for k, v in REQUIRED_VARS.items() if not v]
if missing:
    raise ValueError(f"Missing configuration: {', '.join(missing)}")

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

def send_email(subject, body):
    if DRY_RUN:
        logging.info(f"[DRY RUN] Email: {subject} - {body}")
        return
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


async def alert(message):
    logging.warning(message)
    await send_slack_message(message)
    send_email("Database Replication Alert", message)

# ---------------- Core Logic ----------------

# ---------------- Replication Check Functions ----------------
def check_mysql_replication(db):
    try:
        conn = mysql.connector.connect(
            host=db["host"], port=db["port"],
            user=db["user"], password=db["password"], 
            database=db["database"]
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SHOW SLAVE STATUS")
        status = cursor.fetchone()
        cursor.close()
        conn.close()

        if not status:
            return None, "No replication configured"

        lag = status.get("Seconds_Behind_Master")
        if status["Slave_IO_Running"] != "Yes" or status["Slave_SQL_Running"] != "Yes":
            return lag, "Replication stopped"
        return lag, None
    except Exception as e:
        return None, str(e)

def fix_mysql_replication(db):
    if DRY_RUN:
        logging.info(f"[DRY RUN] Would restart MySQL replication on {db['host']}")
        return True
    try:
        conn = mysql.connector.connect(
            host=db["host"], port=db["port"],
            user=db["user"], password=db["password"], database=db["database"]
        )
        cursor = conn.cursor()
        cursor.execute("START SLAVE")
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"MySQL replication restarted on {db['host']}")
        return True
    except Exception as e:
        logging.error(f"MySQL replication restart failed: {e}")
        return False
    
def check_postgres_replication(db):
    try:
        conn = psycopg2.connect(
            host=db["host"], port=db["port"],
            user=db["user"], password=db["password"], dbname=db["database"]
        )
        cursor = conn.cursor()
        cursor.execute("SELECT EXTRACT(EPOCH FROM now() - pg_last_xact_replay_timestamp())::int AS lag;")
        lag = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return lag, None
    except Exception as e:
        return None, str(e)
    
def promote_postgres_standby(db):
    # Requires superuser privileges and proper configuration
    if DRY_RUN:
        logging.info(f"[DRY RUN] Would promote PostgreSQL standby on {db['host']}")
        return True
    try:
        conn = psycopg2.connect(
            host=db["host"], port=db["port"],
            user=db["user"], password=db["password"], dbname=db["database"]
        )
        cursor = conn.cursor()
        cursor.execute("SELECT pg_promote();")
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"PostgreSQL standby promoted on {db['host']}")
        return True
    except Exception as e:
        logging.error(f"PostgreSQL promotion failed: {e}")
        return False

def check_replication(db):
    try:
        if db["type"] == "mysql":
            return check_mysql_replication(db)
        elif db["type"] == "postgresql":
            return check_postgres_replication(db)
        return None, f"Unsupported DB type: {db['type']}"
    except Exception as e:
        return None, str(e)

def fix_replication(db, error_message):
    for _ in range(2):  # retry 2 times
        if db["type"] == "mysql" and "Replication stopped" in error_message:
            if fix_mysql_replication(db):
                return True
        elif db["type"] == "postgresql" and "replication" in error_message.lower():
            if promote_postgres_standby(db):
                return True
        time.sleep(2)
    return False

# ---------------- Main Monitoring Logic ----------------
async def monitor_replication():
    start_time = time.time()
    while (time.time() - start_time) < MONITOR_DURATION:
        alerts = []
        for db in DATABASES:
            lag, error = await asyncio.to_thread(check_replication, db)
            if error:
                alerts.append(f"[{db['type']}@{db['host']}] ERROR: {error}")
                fixed = await asyncio.to_thread(fix_replication, db, error)
                if fixed:
                    alerts.append(f"[{db['type']}@{db['host']}] Corrective action executed successfully.")
                else:
                    alerts.append(f"[{db['type']}@{db['host']}] Corrective action failed.")
            elif lag is None:
                alerts.append(f"[{db['type']}@{db['host']}] Replication not configured.")
            elif lag > REPLICATION_LAG_THRESHOLD:
                alerts.append(f"[{db['type']}@{db['host']}] High replication lag: {lag}s")

        if alerts:
            await alert("\n".join(alerts))
        await asyncio.sleep(5)

    logging.info("Stopped replication monitoring after duration expiry.")

# ---------------- Execution ----------------
if __name__ == "__main__":
    asyncio.run(monitor_replication())