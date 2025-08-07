# Use case: Log Rotation & Cleanup with Uploads to Cloud
### Logging module → using logging for structured logs.
### File compression → Compress rotated logs with gzip to save disk space.
### Retry mechanism → If a file is locked/busy, retry before skipping.
### Configuration variables → Easier to modify (retention period, log path, backup path).
### Cross-platform safe → Works on Linux and Windows (if absolute paths are adapted).
### AWS S3: Uses boto3 to push compressed logs.
### Azure Blob: Uses azure-storage-blob library.
### Config Switch: Choose CLOUD_PROVIDER = "S3" or "AZURE" without changing core logic.
### Compression before upload: Reduces size and cost of storage.
###  Retry logic still applies for local file handling.

import os
import shutil
import gzip
import time
import logging
from datetime import datetime, timedelta
from utility.devops_library import setup_safe_logging

# ---------------- Configuration ----------------
LOG_FILES = ("/var/log/app1.log", "/var/log/app2.log", "/var/log/app3.log")
LOG_BACKUP_DIR = "/var/log/archive"
RETENTION_DAYS = 7
RETRY_ATTEMPTS = 3
RETRY_DELAY = 2  # seconds

# Choose CLOUD_PROVIDER = "S3" or "AZURE"
CLOUD_PROVIDER = "S3"

# AWS S3 Config
S3_BUCKET = "my-log-backup-bucket"
S3_PREFIX = "logs/"

# Azure Blob Config
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=youraccount;AccountKey=yourkey;EndpointSuffix=core.windows.net"
AZURE_CONTAINER = "logs"

# ---------------- Logging Setup ----------------
# Set up logging
log_path = setup_safe_logging("log_rotation_script.log")

# Log something
logging.info("Log setup complete. Using file: %s", log_path)

# ---------------- Cloud Clients ----------------
s3_client = None
azure_container_client = None

try:
    if CLOUD_PROVIDER == "S3":
        import boto3
        s3_client = boto3.client("s3")
    elif CLOUD_PROVIDER == "AZURE":
        from azure.storage.blob import BlobServiceClient
        azure_blob_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        azure_container_client = azure_blob_client.get_container_client(AZURE_CONTAINER)
        azure_container_client.create_container(exist_ok=True)
except ModuleNotFoundError as e:
    logging.error(f"Required cloud library missing: {e.name}. Cloud upload disabled.")
    CLOUD_PROVIDER = None  # Disable cloud uploads gracefully

# ---------------- Core Functions ----------------
def rotate_log(log_file):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = os.path.join(LOG_BACKUP_DIR, os.path.basename(log_file) + "." + timestamp)

    # Retry mechanism for file access issues
    for attempt in range(RETRY_ATTEMPTS):
        try:
            shutil.copy2(log_file, archive_name)
            open(log_file, 'w').close() # truncate original log
            compressed = compress_log(archive_name)
            logging.info(f"Rotated and compressed: {compressed}")
            upload_to_cloud(compressed) # cloud
            return
        except PermissionError as e:
            logging.error(f"Permission denied when rotating {log_file}: {e}")
            return
        except Exception as e:
            logging.warning(f"Attempt {attempt+1} failed for {log_file}: {e}")
            time.sleep(RETRY_DELAY)
    logging.error(f"Failed to rotate log after {RETRY_ATTEMPTS} attempts: {log_file}")

def compress_log(file_path):
    compressed_path = file_path + '.gz'
    with open(file_path, 'rb') as f_in:
        with gzip.open(compressed_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(file_path) # remove uncompressed copy
    return compressed_path

def upload_to_cloud(file_path):
    if CLOUD_PROVIDER == "S3" and s3_client:
        try:
            s3_key = S3_PREFIX + os.path.basename(file_path)
            s3_client.upload_file(file_path, S3_BUCKET, s3_key)
            logging.info(f"Uploaded to S3: s3://{S3_BUCKET}/{s3_key}")
        except PermissionError as e:
            logging.error(f"Permission denied uploading {file_path}: {e}")
        except Exception as e:
            logging.error(f"Failed to upload {file_path} to S3: {e}")
    elif CLOUD_PROVIDER == "AZURE" and azure_container_client:
        try:
            blob_client = azure_container_client.get_blob_client(os.path.basename(file_path))
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
            logging.info(f"Uploaded to Azure Blob: {os.path.basename(file_path)}")
        except PermissionError as e:
            logging.error(f"Permission denied uploading {file_path}: {e}")
        except Exception as e:
            logging.error(f"Failed to upload {file_path} to Azure Blob: {e}")
    elif CLOUD_PROVIDER is None:
        logging.warning(f"Cloud upload skipped for {file_path} (cloud module missing or disabled)")

def cleanup_old_logs():
    cutoff = datetime.now() - timedelta(days=RETENTION_DAYS)
    try:
        for file in os.listdir(LOG_BACKUP_DIR):
            full_path = os.path.join(LOG_BACKUP_DIR, file)
            if os.path.isfile(full_path):
                file_time = datetime.fromtimestamp(os.path.getmtime(full_path))
                if file_time < cutoff:
                    os.remove(full_path)
                    logging.info(f"Deleted old log: {full_path}")
    except PermissionError as e:
        logging.error(f"Permission denied during cleanup: {e}")

# ---------------- Script Execution ----------------
def main():
    global LOG_BACKUP_DIR

    # Check backup directory permission before using
    if not os.access(os.path.dirname(LOG_BACKUP_DIR) or ".", os.W_OK):
        fallback_dir = os.path.join(os.getcwd(), "archive")
        print(f"Permission denied for {LOG_BACKUP_DIR}, using fallback: {fallback_dir}")
        logging.warning(f"Permission denied for {LOG_BACKUP_DIR}. Falling back to {fallback_dir}")
        LOG_BACKUP_DIR = fallback_dir

    os.makedirs(LOG_BACKUP_DIR, exist_ok=True)

    logging.info("Starting log rotation & cloud upload process")

    for log in LOG_FILES:
        if os.path.exists(log):
            rotate_log(log)
        else:
            logging.warning(f"Log file not found: {log}")

    cleanup_old_logs()
    logging.info("Log rotation and cloud upload completed successfully")

if __name__ == "__main__":
    main()
