# Use Case: Monitoring and Reporting:
# In scenarios where you need to gather data or perform checks on multiple systems, a "for" loop is handy. 
## monitoring server resources across multiple machines:
## We’ll check CPU and memory usage on multiple servers.
## Handle errors gracefully (like server unreachable).
## Collect results into a report.
## Uses Paramiko (SSH client) to run commands remotely.
import paramiko
import logging
from datetime import datetime

# ---------------- Logging Setup ----------------
# Configure logging to write to a file and also print to console
log_file = "server_monitoring.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

# ---------------- Server List ----------------
# List of servers with SSH connection details
servers = [
    {"host": "server1.example.com", "user": "devops", "password": "secret"},
    {"host": "server2.example.com", "user": "devops", "password": "secret"},
    {"host": "server3.example.com", "user": "devops", "password": "secret"},
]

# ---------------- Monitoring Commands ----------------
# Commands to run on each server to gather resource information
commands = {
    "uptime": "uptime",                  # System uptime and load averages
    "memory": "free -m | grep Mem",      # Memory usage in megabytes
    "disk": "df -h /"                    # Disk usage of root partition in human-readable format
}

def run_ssh_command(host, user, password, cmd):
    """
    Connects to a remote server via SSH and executes a command.
    Returns the output or error message.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown hosts
    try:
        # Connect to the server with a 5-second timeout
        client.connect(host, username=user, password=password, timeout=5)
        # Execute the command
        stdin, stdout, stderr = client.exec_command(cmd)
        # Read standard output and error streams
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        if error:
            logging.error(f"[{host}] Error running '{cmd}': {error}")
            return f"ERROR: {error}"
        return output
    except Exception as e:
        # Log any exceptions (e.g., connection failure)
        logging.error(f"[{host}] Connection/Command error: {e}")
        return f"ERROR: {e}"
    finally:
        client.close()  # Always close the SSH connection

def monitor_servers(server_list, command_dict):
    """
    Loops through all servers and executes the monitoring commands.
    Collects results in a list of dictionaries.
    """
    report = []
    for server in server_list:
        host = server["host"]
        logging.info(f"Monitoring {host}")
        server_report = {"host": host, "results": {}}
        # Run each command and store its output
        for key, cmd in command_dict.items():
            result = run_ssh_command(host, server["user"], server["password"], cmd)
            server_report["results"][key] = result
            logging.info(f"[{host}] {key} -> {result}")
        report.append(server_report)
    return report

def save_report(report_data):
    """
    Saves the monitoring data into a timestamped text file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"monitoring_report_{timestamp}.txt"
    try:
        with open(filename, "w") as f:
            # Write server data and command outputs to the file
            for server_data in report_data:
                f.write(f"Server: {server_data['host']}\n")
                for metric, output in server_data["results"].items():
                    f.write(f"  {metric}:\n    {output}\n")
                f.write("\n")
        logging.info(f"Monitoring report saved to {filename}")
        print(f"Monitoring report saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving report: {e}")
        print(f"Error saving report: {e}")

# ---------------- Script Execution ----------------
def main():
    logging.info("===== Starting Server Monitoring =====")
    # Perform the monitoring on all servers
    report = monitor_servers(servers, commands)
    # Save the collected data into a report file
    save_report(report)
    logging.info("===== Monitoring Completed =====")

if __name__ == "__main__":
    main()