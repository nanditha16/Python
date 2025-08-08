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