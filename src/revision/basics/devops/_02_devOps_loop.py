# Use case: Provisioning servers & installing monitoring agent
## A tuple to store server names (immutable list of servers).
## A try/except block to handle provisioning errors safely.

def provision_server(server):
    # Simulate provisioning logic
    if server == "server3":   # Simulating one server failure
        raise Exception("Connection timeout")
    return f"Monitoring agent installed on {server}"

# Use case: Deploy Configuration to Multiple Environments
## Tuple for environments (dev, staging, prod).
## A simulated deployment function.
## Error handling with try/except.
def deploy_configuration(env):
    # Simulate deployment
    if env == "staging":  # Simulate an error for demonstration
        raise Exception("Deployment pipeline failed")
    return f"Configuration deployed successfully to {env}"

# Use case: Backup & Restore for Multiple Databases
## Tuple to list databases.
## Separate functions for backup and restore.
## try/except for handling errors gracefully.
def backup_database(db):
    # Simulated backup
    if db == "orders_db":   # simulate one failure
        raise Exception("Disk full during backup")
    return f"Backup completed for {db}"

def restore_database(db):
    # Simulated restore
    return f"Restore completed for {db}"

# Use case: Log Rotation & Cleanup
## Use a tuple to store log file paths.
## Implement rotation by renaming the current log file to include a timestamp.
## Delete old logs beyond a certain retention period.
## Add error handling for robustness.





if __name__ == "__main__":
     # Use case: Provisioning servers & installing monitoring agent
     servers = ("server1", "server2", "server3", "server4")
     for server in servers:
         try:
             result = provision_server(server)
             print(result)
         except Exception as e:
             print(f"Error provisioning {server}: {e}")

     # Use case: Deploy Configuration to Multiple Environments
     environments = ("development", "staging", "production")
     for env in environments:
         try:
             result = deploy_configuration(env)
             print(result)
         except Exception as e:
             print(f"Error deploying to {env}: {e}")
     
     # Use case: Backup & Restore for Multiple Databases
     databases = ("user_db", "orders_db", "inventory_db") 
     # Backup operation
     print("Starting backup operations...")
     for db in databases:
         try:
             result = backup_database(db)
             print(result)
         except Exception as e:
             print(f"Error backing up {db}: {e}")

    # Restore operation
     print("\nStarting restore operations...")
     for db in databases:
         try:
             result = restore_database(db)
             print(result)
         except Exception as e:
             print(f"Error restoring {db}: {e}")