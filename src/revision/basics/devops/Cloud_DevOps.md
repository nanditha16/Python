# Cloud (AWS) and DevOps Basics:

### Pre Requisition:

1. Recommended for Ubuntu (Codespaces default) – Install AWS CLI v2 
 **Step 1** : 
    ```
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    ```
 **Step 2** : Verify
    ```
    aws --version
 **Step 3** : Clean Up Installation Files (optional) 
    ```
    rm -rf awscliv2.zip aws/
    ```
 **Step 4** : Update if any thing is missing
    ```
    sudo apt-get update
    sudo apt-get install unzip -y
 **Step 5** : configuring AWS credentials inside Codespaces 
    - option 1: Recommended (as it will need details with your aws account - AWS Access Key ID, AWS Secret Access Key, Default region (e.g., us-east-1), Output format (e.g., json))
    ```
        aws configure
    ```
    - option 2: You can also Use Environment Variables and set them temporarily in the terminal
    ```
    export AWS_ACCESS_KEY_ID=your_access_key
    export AWS_SECRET_ACCESS_KEY=your_secret_key
    export AWS_DEFAULT_REGION=us-east-1
    ```
    - option 3: Use .env file and Load environment variables from .env file (local setup) 
    ```
    from dotenv import load_dotenv
    load_dotenv()
    ```
2. Create Developer IAM Role with Limited Access for DevOps and Cloud to be used | Aautomation with Terraform or CloudFormation version of this setup.
**Step 1** : Create a DevOps IAM Role
   - Sign in as root (only this once).
   - Go to IAM → Roles → Create Role
   - Select trusted entity:
      - Choose AWS account
      - If user will assume this role via CLI or console, choose “This account”
   - Use Case: Select “Custom Trust Policy” if necessary.
   - Click Next and attach only necessary policies (e.g., AmazonEC2ReadOnlyAccess, or custom policies).
   - Name it: DevOpsLimitedRole
   - Review and Create Role
**Step 2** : Create the IAM User
   - Go to IAM → Users → Add user
   - Enter name: DevOpsUser
   - Select Access type:
      - AWS Management Console
      - Programmatic Access (if using CLI/API)
   - Under Set Permissions:
      - Choose “Attach existing policies directly” → DO NOT attach admin or broad policies.
      - Instead, skip this step and attach permissions later via inline policy or role assumption.
**Step 3** : Attach Minimal Inline Policy
   - To allow the user to assume the role
**Step 4** : Add Scoped Access Policy to the Role
   - Create a custom policy (e.g., limited S3, EC2, Lambda access):
**Step 5** : Enable MFA on the user account.
**Step 6** : Use IAM Access Analyzer to validate permission boundaries.
**Step 7** : Periodically review CloudTrail logs and IAM Access Advisor.

### AWS resource:

1. EC2 (Virtual Server) 
   - Starting, stopping, and terminating instances.
   - Monitoring instance performance and utilization.
2. Lambda (Serverless): 
   - Cost Optimization Basic Example:
   ```
   import boto3

   def lambda_handler(event, context):
      ec2 = boto3.client('ec2')

      # Get all running EC2 instance IDs
      active_instance_ids = get_active_instance_ids(ec2)

      # Iterate through all snapshots using pagination
      for snapshot in get_all_snapshots(ec2):
         snapshot_id = snapshot['SnapshotId']
         volume_id = snapshot.get('VolumeId')

         if not volume_id:
               delete_snapshot(ec2, snapshot_id, "not attached to any volume. Deleted.")
               continue

         try:
               volume = ec2.describe_volumes(VolumeIds=[volume_id])['Volumes'][0]
               attachments = volume.get('Attachments', [])

               attached_instance_ids = {
                  att['InstanceId'] for att in attachments if 'InstanceId' in att
               }

               if not attached_instance_ids & active_instance_ids:
                  delete_snapshot(ec2, snapshot_id, "volume not attached to any running instance. Deleted.")

         except ec2.exceptions.ClientError as e:
               if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                  delete_snapshot(ec2, snapshot_id, "associated volume not found. Deleted.")


   def get_active_instance_ids(ec2):
      paginator = ec2.get_paginator('describe_instances')
      active_ids = set()

      for page in paginator.paginate(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
         for reservation in page['Reservations']:
               for instance in reservation['Instances']:
                  active_ids.add(instance['InstanceId'])

      return active_ids

   def get_all_snapshots(ec2):
      paginator = ec2.get_paginator('describe_snapshots')
      for page in paginator.paginate(OwnerIds=['self']):
         for snapshot in page['Snapshots']:
               yield snapshot

   def delete_snapshot(ec2_client, snapshot_id, reason):
      ec2_client.delete_snapshot(SnapshotId=snapshot_id)
      print(f"Deleted snapshot {snapshot_id}: {reason}")
   ```
   - Security/Compliance : Device Protection Across Multiple Locations