"""
Use Case: Config Updater - Reads and updates configuration files (JSON or YAML) for multiple VMs (Linux/Windows).
-------------------------------------------------------
DevOps engineers often monitor database replication to ensure data consistency.
This script uses a while loop to:
1. Backs up before changing (safety first - Backup before saving)
2. Error handling for missing files, Input validation, invalid config format
3. Uses configparser (standard Python library)
4. Logging instead of print (ready for CI/CD pipelines)
5. Easily extensible to support JSON/YAML
6. Supports multiple VM types (Linux, Windows).
7. Reads and updates JSON or YAML config files.
8. Can handle bulk updates for multiple VMs.

Example: Updating VM parameters like hostname, IP, environment variables, etc.
- Search for a specific key (in this case, inside VMs.linux or VMs.windows)
- Update only the matching section without breaking other config fields [Dynamic field updates - Improved CLI argument handling]
- Write the updated file back in the same format it was read

Usage Examples:
---------------
Single Update:
    Update a VM’s IP address:
        python _12_devOps_simple_file_update.py --file config.json --vm_type linux --hostname linux01 --field ip --value 10.0.0.99
        python _12_devOps_simple_file_update.py --file config.yaml --vm_type windows --hostname win01 --field ip --value 192.168.1.50

    Update a VM’s environment:
        python _12_devOps_simple_file_update.py --file config.json --vm_type linux --hostname linux01 --field env --value staging

    Update a custom field (e.g., owner):
        python _12_devOps_simple_file_update.py --file config.yaml --vm_type windows --hostname win01 --field owner --value nanditha

Bulk Update from CSV:
    python _12_devOps_simple_file_update.py --file config.json --bulk_file bulk_updates.csv

Bulk Update from YAML:
    python _12_devOps_simple_file_update.py --file config.yaml --bulk_file bulk_updates.yaml
"""
import os
import sys
import json
import yaml
import csv
import logging
import argparse
import re
from typing import Any

from utility.devops_library import setup_safe_logging

# ---------------- Logging Setup ----------------
# Set up logging
log_path = setup_safe_logging("config_updater.log")

# ---------------- Utility Functions ----------------
def is_valid_ip(ip: str) -> bool:
    """Validate IP address format."""
    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    return re.match(pattern, ip) is not None

def backup_config(file_path: str):
    """Create a backup of the config file."""
    try:
        backup_path = f"{file_path}.bak"
        with open(file_path, "r") as original, open(backup_path, "w") as backup:
            backup.write(original.read())
        logging.info(f"Backup created at {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")


# ---------------- Core Logic - File I/O ----------------
# Config File Loader
def load_config(file_path: str) -> Any:
    """Load JSON or YAML config file."""
    try:
        with open(file_path, "r") as f:
            if file_path.endswith(".json"):
                return json.load(f)
            elif file_path.endswith((".yaml", ".yml")):
                return yaml.safe_load(f)
            else:
                raise ValueError("Unsupported file format. Use .json or .yaml/.yml")
    except FileNotFoundError:
        logging.error(f"Config file not found: {file_path}")
        sys.exit(1)
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        logging.error(f"Error parsing config file {file_path}: {e}")
        sys.exit(1)


# Config File Writer
def save_config(file_path: str, data: Any):
    """Save JSON or YAML config file."""
    try:
        with open(file_path, "w") as f:
            if file_path.endswith(".json"):
                json.dump(data, f, indent=2)
            else:
                yaml.safe_dump(data, f, sort_keys=False)
        logging.info(f"Config file updated successfully: {file_path}")
    except Exception as e:
        logging.error(f"Error saving config file: {e}")
        sys.exit(1)

# ---------------- Update Logic ----------------
# Update any field for a specific VM.
def update_vm_field(config_data: dict, vm_type: str, hostname: str, field: str, value: str) -> bool:
    """Update any field for a specific VM."""
    try:
        # vm_list = config_data.get("VMs", {}).get(vm_type, [])
        vm_section = config_data.get("VMs", {})
        logging.debug(f"VM section structure: {vm_section}")
        if not isinstance(vm_section, dict):
            logging.error("Invalid config format: 'VMs' should be a dictionary")
            return False

        vm_list = vm_section.get(vm_type, [])
        if not isinstance(vm_list, list):
            logging.error(f"Invalid config format: 'VMs.{vm_type}' should be a list")
            return False


        for vm in vm_list:
            if vm.get("hostname") == hostname:
                old_value = vm.get(field, "Not set")
                if field == "ip" and not is_valid_ip(value):
                    logging.error(f"Invalid IP address format: {value}")
                    return False
                vm[field] = value
                logging.info(f"Updated {vm_type} VM '{hostname}' field '{field}' from '{old_value}' to '{value}'")
                return True
        logging.warning(f"No matching {vm_type} VM found with hostname '{hostname}'")
        return False
    except Exception as e:
        logging.error(f"Error updating VM field: {e}")
        return False

# Bulk Update Logic
def bulk_update(config_data: dict, bulk_file: str):
    """Apply bulk updates from CSV or YAML."""
    try:
        if bulk_file.endswith(".csv"):
            with open(bulk_file, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    update_vm_field(config_data, row["vm_type"], row["hostname"], row["field"], row["value"])

        elif bulk_file.endswith((".yaml", ".yml")):
            with open(bulk_file, "r") as f:
                bulk_data = yaml.safe_load(f)
                for entry in bulk_data:
                    update_vm_field(config_data, entry["vm_type"], entry["hostname"], entry["field"], entry["value"])

        else:
            logging.error("Bulk update file must be CSV or YAML format")
            sys.exit(1)
    except FileNotFoundError:
        logging.error(f"Bulk update file not found: {bulk_file}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error processing bulk update file: {e}")
        sys.exit(1)

# ---------------- Execution ----------------
def main():
    parser = argparse.ArgumentParser(description="Update VM configurations in JSON/YAML config files")
    parser.add_argument("--file", required=True, help="Path to the config file (JSON/YAML)")
    parser.add_argument("--vm_type", choices=["linux", "windows"], help="Type of VM")
    parser.add_argument("--hostname", help="Hostname of the VM to update")
    parser.add_argument("--field", help="Field to update (e.g., ip, env)")
    parser.add_argument("--value", help="New value for the field")
    parser.add_argument("--bulk_file", help="CSV/YAML file for bulk updates")

    args = parser.parse_args()
    config_data = load_config(args.file)
    backup_config(args.file)

    if args.bulk_file:
        # bulk file (bulk_updates.csv) is just a set of instructions
        # it’s not meant to be modified. 
        # The script reads it, applies the updates to the target config file (config.json), and saves the result.
        bulk_update(config_data, args.bulk_file)
    elif args.vm_type and args.hostname and args.field and args.value:
        updated = update_vm_field(config_data, args.vm_type, args.hostname, args.field, args.value)
        if not updated:
            sys.exit(1)
    else:
        logging.error("Provide either --bulk_file OR all of --vm_type, --hostname, --field, and --value")
        sys.exit(1)

    save_config(args.file, config_data)

if __name__ == "__main__":
    main()
