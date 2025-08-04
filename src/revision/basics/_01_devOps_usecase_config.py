# Using Variables to Store and Manipulate Configuration Data in a DevOps Context

# This script demonstrates how to use variables to store and manipulate configuration data in a DevOps context.
# Note: This is a simplified example for educational purposes.
# Import necessary modules
import os
import json
import logging

# Set up logging early for error reporting
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define configuration variables
config = {
    "app_name": "MyApp",
    "version": "1.0",
    "allowed_hosts": ["localhost", "example.com"],
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": os.environ.get("DB_USER", "db_user"),
        "password": os.environ.get("DB_PASSWORD", "db_password")  # Use env vars for sensitive data
    },
    "is_https_enabled": True,
    "max_connections": 1000,
    "timeout": 30,
    "log_level": "INFO",
    "debug": False
}

# Save configuration to a JSON file with error handling
try:
    with open("config.json", "w") as config_file:
        # Do not write sensitive data like passwords in plaintext in production can use HashiCorp Vault or similar tools
        safe_config = config.copy()
        safe_config["database"] = safe_config["database"].copy()
        safe_config["database"]["password"] = "****"  # Mask password
        json.dump(safe_config, config_file)
except (IOError, OSError) as e:
    logger.error(f"Failed to write config.json: {e}")
    raise

# Load configuration from a JSON file with error handling
try:
    with open("config.json", "r") as config_file:
        loaded_config = json.load(config_file)
except (IOError, OSError, json.JSONDecodeError) as e:
    logger.error(f"Failed to load config.json: {e}")
    loaded_config = {}

if not loaded_config:
    logger.error("Configuration could not be loaded. Exiting.")
    exit(1)

# Print loaded configuration (mask sensitive info)
print("Loaded Configuration:")
for key, value in loaded_config.items():
    if key == "database":
        db_info = value.copy()
        db_info["password"] = "****"
        print(f"  {key}: {db_info}")
    else:
        print(f"  {key}: {value}")

# Example of using a variable in a conditional statement
if loaded_config.get("debug"):
    print("Debug mode is enabled.")
else:
    print("Debug mode is disabled.")

# Example of using a variable in a loop
for host in loaded_config.get("allowed_hosts", []):
    print(f"Connecting to {host}...")

# Example of using a variable in a function
def connect_to_database(db_config):
    try:
        print(f"Connecting to database at {db_config['host']}:{db_config['port']} as {db_config['username']}...")
        # Simulate a connection
        if loaded_config.get("is_https_enabled"):
            print("Using HTTPS for secure connection.")
        else:
            print("Using HTTP for connection.")
        # Never print or log passwords
    except KeyError as e:
        logger.error(f"Database config missing key: {e}")

connect_to_database(loaded_config.get("database", {}))

# Example of using a variable in an environment variable
os.environ["APP_NAME"] = loaded_config.get("app_name", "MyApp")
print(f"Environment variable APP_NAME set to: {os.environ['APP_NAME']}")

# Example of using a variable in a command (avoid shell injection)
import shlex
host = shlex.quote(loaded_config.get("allowed_hosts", ["localhost"])[0])
command = f"curl -X GET https://{host}/api/v1/status"
print(f"Executing command: {command}")
# Note: In a real DevOps context, use subprocess.run with a list for safety
# import subprocess
# subprocess.run(["curl", "-X", "GET", f"https://{host}/api/v1/status"])

# Example of using a variable in a deployment script (mask sensitive info)
deployment_script = f"""#!/bin/bash
echo "Deploying {loaded_config.get('app_name', '')} version {loaded_config.get('version', '')}..."
echo "Connecting to database at {loaded_config.get('database', {}).get('host', '')}:{loaded_config.get('database', {}).get('port', '')}..."
if {str(loaded_config.get('is_https_enabled', False)).lower()} == "true"; then
    echo "Using HTTPS for secure connection."
else
    echo "Using HTTP for connection."
fi
echo "Max connections allowed: {loaded_config.get('max_connections', '')}"
echo "Timeout set to {loaded_config.get('timeout', '')} seconds."
echo "Log level set to {loaded_config.get('log_level', '')}."
"""

# Save the deployment script to a file with error handling
try:
    with open("deploy.sh", "w") as script_file:
        script_file.write(deployment_script)
    os.chmod("deploy.sh", 0o755)
    print("Deployment script 'deploy.sh' has been created and is ready to execute.")
except (IOError, OSError) as e:
    logger.error(f"Failed to create deployment script: {e}")

logger.info("Deployment script 'deploy.sh' has been created and is ready to execute.")
# Note: This script is a simplified example and should not be used in production without proper security measures.
# End of the script
# This script demonstrates how to use variables to store and manipulate configuration data in a DevOps context
# and includes error handling, logging, and best practices for sensitive data management.