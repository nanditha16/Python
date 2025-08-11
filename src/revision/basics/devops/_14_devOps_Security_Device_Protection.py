
# Use Case: Device Protection Across Multiple Locations — Lambda-integrated solution for organizational security.

# Overview:
# Your organization has many devices distributed across multiple locations.
# You need a scalable and automated solution to help protect these devices from unauthorized access, misconfiguration, and exposure.
# This solution can be built using AWS services and Lambda to monitor, audit, and enforce security policies.
# 1. Use AWS Systems Manager to register and manage devices (via SSM Agent).
# 2. Use AWS Config to track configuration changes and compliance across regions.
# 3. Use AWS Lambda to respond to non-compliant states (e.g., missing patches, open ports).
# 4. Use AWS IoT Device Defender for edge devices to monitor behavior and detect anomalies.
# 5. Use tag-based policies to group devices by location, department, or sensitivity.
# 6. Store audit logs and alerts in Amazon S3 or CloudWatch Logs for centralized visibility.
# 7. Send notifications via SNS or Slack when a device violates policy or becomes vulnerable.
# 8. Integrate with AWS Security Hub for consolidated security findings across services.
# 9. Schedule periodic scans and patching using EventBridge and Lambda automation.
# 10. Ensure IAM roles and permissions are scoped to device management and remediation tasks.

# IAM Permissions Required:
EventBridge rules (examples)
# 1) Scheduled scans & patching
# {
#   "Name": "device-protection-scan-daily",
#   "ScheduleExpression": "cron(0 3 * * ? *)",
#   "State": "ENABLED",
#   "Targets": [{
#     "Arn": "<lambda-arn>",
#     "Id": "device-protection-lambda",
#     "Input": "{\"source\":\"custom.deviceprotection\",\"detail\":{\"action\":\"Scan\"}}"
#   }]
# }
# 
# 2) AWS Config -> non-compliance
# Event pattern:
# {
#   "source": ["aws.config"],
#   "detail-type": ["Config Rules Compliance Change"],
#   "detail": {
#     "newEvaluationResult": ["NON_COMPLIANT"]
#   }
# }
# 
# 3) Security Hub -> findings
# {
#   "source": ["aws.securityhub"],
#   "detail-type": ["Security Hub Findings - Imported"]
# }
# 
# 4) IoT Device Defender
# {
#   "source": ["aws.iot"],
#   "detail-type": ["AWS IoT Device Defender Metric Alarm", "AWS IoT Device Defender ML Detect Violation"]
# }

# Attach to the Lambda’s execution role (tighten regions/resources as you deploy):
# (least-privilege starting point):
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     { "Effect": "Allow", "Action": ["logs:CreateLogGroup","logs:CreateLogStream","logs:PutLogEvents"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["ec2:DescribeInstances"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["ssm:SendCommand","ssm:DescribeInstanceInformation","ssm:ListCommandInvocations","ssm:ListCommands"], 
#       "Resource": "*" 
#     },
#     { "Effect": "Allow", "Action": ["ssm:SendCommand"], 
#       "Resource": "arn:aws:ssm:*:*:document/*" 
#     },
#     { "Effect": "Allow", "Action": ["sns:Publish"], "Resource": "<your-sns-topic-arn>" },
#     { "Effect": "Allow", "Action": ["s3:PutObject"], "Resource": "arn:aws:s3:::<your-audit-bucket>/*" },
#     { "Effect": "Allow", "Action": ["securityhub:BatchImportFindings"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["sts:GetCallerIdentity"], "Resource": "*" }
#   ]
# }
# IAM Permissions Required (Lambda Execution Role):
# Ensure the Lambda role includes the following permissions:
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     { "Effect": "Allow", "Action": ["ssm:DescribeInstanceInformation", "ssm:SendCommand"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["config:GetComplianceDetailsByResource", "config:DescribeConfigRules"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["iot:DescribeThing", "iot:ListThings"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["securityhub:GetFindings"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["logs:CreateLogStream", "logs:PutLogEvents"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["sns:Publish"], "Resource": "*" },
#     { "Effect": "Allow", "Action": ["s3:PutObject"], "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*" }
#   ]
# }

# Environment Variables:
# Set these in the Lambda configuration to control behavior:
# - REGIONS — Comma-separated list of AWS regions to scan (optional; scans all if unset)
# - APPLY — Set to true to release EIPs; false for dry-run mode
# - MIN_AGE_DAYS — Minimum age (in days) for EIPs to be considered for release
# - EXCLUDE_TAGS — Comma-separated tag filters (e.g., DoNotDelete=*)
# - S3_BUCKET — Name of the S3 bucket to store the CSV report
# - S3_PREFIX — S3 key prefix for the report file (e.g., eip-cleanup/)
# - ONLY_WRITE_IF_CHANGES — If true, skips writing report if no EIPs were released or found

# Output:
# - CSV report in S3 with fields:
#   region, allocation_id, public_ip, domain, name_tag, age_days, in_use, excluded_by_tag, note, released, scan_timestamp, account_id
# - CloudWatch metrics:
#   CandidatesFound, Released

# Environment Variables:
# - DEVICE_TAG_FILTER — Tag-based filter to scope which devices are monitored (e.g., Location=Toronto)
# - COMPLIANCE_RULES — List of AWS Config rule names to enforce
# - ALERT_TOPIC_ARN — SNS topic ARN for sending alerts
# - S3_BUCKET — Bucket to store audit logs and reports
# - SCAN_INTERVAL — Frequency of scans (e.g., daily, weekly)

# Output:
# - Audit logs stored in S3 or CloudWatch Logs
# - Alerts sent via SNS or Slack
# - Compliance reports generated and optionally stored
# - Automated remediation actions triggered by Lambda

# Deployment Notes:
# - Recommended to trigger via EventBridge on a schedule or Config rule change.
# - Use Systems Manager Inventory for device visibility.
# - Use Lambda versions and aliases for safe deployment and rollback.


import json
import os
import time
import uuid
import logging
from datetime import datetime, timezone

import boto3
import urllib.request
from dotenv import load_dotenv
from utility.devops_library import setup_safe_logging

# ---------------- Load Environment ----------------
load_dotenv()

# ---------------- Logging Setup ----------------
log_path = setup_safe_logging("aws_Security_Device_Protection.log")
logging.info("Log setup complete. Using file: %s", log_path)

logger.setLevel(logging.INFO)

# ---------------- Configurations ----------------
AUDIT_BUCKET            = os.getenv("AUDIT_BUCKET", "")
SNS_TOPIC_ARN           = os.getenv("SNS_TOPIC_ARN", "")
SLACK_WEBHOOK_URL       = os.getenv("SLACK_WEBHOOK_URL", "")
SECURITY_HUB_ENABLED    = os.getenv("SECURITY_HUB_ENABLED", "true").lower() == "true"
SCOPE_TAG_KEY           = os.getenv("SCOPE_TAG_KEY", "SecurityScope")
SCOPE_TAG_VALUES_JSON   = os.getenv("SCOPE_TAG_VALUES_JSON", '["prod","pci","hipaa","hqloc"]')
DEFAULT_PATCH_GROUP     = os.getenv("DEFAULT_PATCH_GROUP", "prod")
REGION                  = os.getenv("AWS_REGION", "us-east-1")

# Optional: map locations/departments/sensitivity -> required policies
# Example policy bundle names used to select remediation playbooks/SSM docs
POLICY_MAP = {
    "location:nyc": {"patch": True, "require_ebs_encrypt": True, "close_ports": [22], "cis_level": 1},
    "location:sv":  {"patch": True, "close_ports": [22, 3389], "cis_level": 2},
    "dept:finance": {"patch": True, "require_ebs_encrypt": True, "close_ports": [22], "extra_audit": True},
    "sensitivity:pci": {"patch": True, "require_ebs_encrypt": True, "close_ports": [22, 3389], "cis_level": 2},
}

# ---------------- Clients ----------------
ssm          = boto3.client("ssm")
ec2          = boto3.client("ec2")
s3           = boto3.client("s3")
sns          = boto3.client("sns")
securityhub  = boto3.client("securityhub") if SECURITY_HUB_ENABLED else None


# ---------------- Helpers ----------------

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def put_audit_log(payload: dict):
    """Write structured audit event to S3 (if configured) and CloudWatch Logs."""
    payload = dict(payload)  # shallow copy
    payload.setdefault("timestamp", now_iso())
    logger.info(json.dumps({"audit": payload}))
    if AUDIT_BUCKET:
        key = f"device-protection/{datetime.utcnow().strftime('%Y/%m/%d')}/{uuid.uuid4()}.json"
        s3.put_object(Bucket=AUDIT_BUCKET, Key=key, Body=json.dumps(payload).encode("utf-8"))
        return {"bucket": AUDIT_BUCKET, "key": key}
    return None

def notify(subject: str, message: str, severity: str = "MEDIUM"):
    """Send notifications to SNS and/or Slack."""
    # SNS
    if SNS_TOPIC_ARN:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"[{severity}] {subject}",
            Message=message
        )
    # Slack
    if SLACK_WEBHOOK_URL:
        data = json.dumps({"text": f"*{subject}* ({severity})\n{message}"}).encode("utf-8")
        req = urllib.request.Request(SLACK_WEBHOOK_URL, data=data, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=3) as resp:
                _ = resp.read()
        except Exception as e:
            logger.warning(f"Slack notification failed: {e}")

def get_instance_tags(instance_id: str) -> dict:
    """Return tags for an EC2 instance as a dict."""
    resp = ec2.describe_instances(InstanceIds=[instance_id])
    reservations = resp.get("Reservations", [])
    if not reservations or not reservations[0]["Instances"]:
        return {}
    tags = reservations[0]["Instances"][0].get("Tags", [])
    return {t["Key"]: t["Value"] for t in tags}

def tags_to_policy_keys(tags: dict):
    """Derive policy keys like 'location:nyc' or 'dept:finance' from tags."""
    keys = []
    # Example tag keys -> policy keys
    if v := tags.get("Location"):
        keys.append(f"location:{v.lower()}")
    if v := tags.get("Department"):
        keys.append(f"dept:{v.lower()}")
    if v := tags.get("Sensitivity"):
        keys.append(f"sensitivity:{v.lower()}")
    return keys

def is_in_scope(tags: dict) -> bool:
    """Scope by a single tag key and a set of allowed values (tag-based policies)."""
    try:
        allowed = set(json.loads(SCOPE_TAG_VALUES_JSON))
    except Exception:
        allowed = set()
    value = tags.get(SCOPE_TAG_KEY)
    return value in allowed if value else False


def ssm_run_patch(instance_ids: list, operation: str = "Install"):
    """
    Run AWS-RunPatchBaseline via SSM.
    operation: 'Scan' or 'Install'
    """
    if not instance_ids:
        return None
    params = {
        "Operation": [operation],
        "SnapshotId": [f"dp-{int(time.time())}"]
    }
    return ssm.send_command(
        InstanceIds=instance_ids,
        DocumentName="AWS-RunPatchBaseline",
        Parameters=params,
        TimeoutSeconds=3600,
        Comment=f"DeviceProtection {operation} patches"
    )

def ssm_close_ports(instance_ids: list, ports: list):
    """
    Example remediation to close ports via SSM.
    You can replace this with your hardened doc: e.g., 'SSM-CloseInboundPorts'
    """
    if not instance_ids or not ports:
        return None
    script = "\n".join([f"ufw deny {p} || true" for p in ports]) + "\nufw reload || true"
    return ssm.send_command(
        InstanceIds=instance_ids,
        DocumentName="AWS-RunShellScript",
        Parameters={"commands": [script]},
        TimeoutSeconds=900,
        Comment=f"Close inbound ports {ports}"
    )

def import_custom_finding(resource_arn: str, title: str, description: str, severity="MEDIUM", types=None):
    if not SECURITY_HUB_ENABLED:
        return
    if types is None:
        types = ["Software and Configuration Checks/Industry Best Practice"]
    finding = {
        "SchemaVersion": "2018-10-08",
        "Id": str(uuid.uuid4()),
        "ProductArn": f"arn:aws:securityhub:{REGION}:{boto3.client('sts').get_caller_identity()['Account']}:product/{boto3.client('sts').get_caller_identity()['Account']}/default",
        "GeneratorId": "device-protection-lambda",
        "AwsAccountId": boto3.client("sts").get_caller_identity()["Account"],
        "Types": types,
        "CreatedAt": now_iso(),
        "UpdatedAt": now_iso(),
        "Severity": {"Label": severity},
        "Title": title,
        "Description": description,
        "Resources": [{"Type": "AwsEc2Instance", "Id": resource_arn}],
        "ProductFields": {"Remediation": "Auto/SSM"}
    }
    securityhub.batch_import_findings(Findings=[finding])

# ---------------- Event routers ---------------- 
def handle_scheduled_scan(event):
    """
    Triggered by EventBridge schedule.
    - Discover in-scope instances via SSM resource data sync (DescribeInstanceInformation)
    - Run patch SCAN (or INSTALL if 'ACTION=Install')
    """
    action = event.get("detail", {}).get("action", os.getenv("SCHEDULE_ACTION", "Scan"))
    paginator = ssm.get_paginator("describe_instance_information")
    targets = []
    for page in paginator.paginate():
        for inst in page.get("InstanceInformationList", []):
            instance_id = inst.get("InstanceId")
            tags = get_instance_tags(instance_id)
            if is_in_scope(tags):
                targets.append(instance_id)

    if not targets:
        put_audit_log({"event": "scheduled-scan", "action": action, "result": "no_targets"})
        return {"status": "ok", "message": "No in-scope instances found."}

    if action.lower() == "scan":
        resp = ssm_run_patch(targets, "Scan")
        msg = f"Triggered patch SCAN on {len(targets)} instances."
    else:
        resp = ssm_run_patch(targets, "Install")
        msg = f"Triggered patch INSTALL on {len(targets)} instances."

    put_audit_log({"event": "scheduled-scan", "action": action, "targets": targets, "ssm_command": resp["Command"]["CommandId"]})
    notify("Scheduled patch operation", msg, "LOW")
    return {"status": "ok", "message": msg, "command_id": resp["Command"]["CommandId"]}


def handle_config_rule_noncompliance(event):
    """
    EventBridge rule target for AWS Config non-compliant evaluations.
    Expect: detail -> (configRuleName, resourceId, resourceType, newEvaluationResult: NON_COMPLIANT)
    """
    detail = event.get("detail", {})
    resource_id = detail.get("resourceId")
    resource_type = detail.get("resourceType", "")
    rule = detail.get("configRuleName", "unknown-rule")

    # Only remediate EC2 instances in this example
    if resource_type != "AWS::EC2::Instance":
        put_audit_log({"event": "config-noncompliance", "resource_type": resource_type, "resource_id": resource_id, "action": "ignored"})
        return {"status": "ignored", "reason": "Unsupported resource type"}

    instance_id = resource_id
    tags = get_instance_tags(instance_id)
    if not is_in_scope(tags):
        put_audit_log({"event": "config-noncompliance", "instance_id": instance_id, "action": "out_of_scope", "tags": tags})
        return {"status": "ignored", "reason": "Out of scope"}

    policy_keys = tags_to_policy_keys(tags)
    active_policy = {}
    for k in policy_keys:
        active_policy |= POLICY_MAP.get(k, {})

    actions = []
    if active_policy.get("patch"):
        resp = ssm_run_patch([instance_id], "Install")
        actions.append({"action": "patch", "command_id": resp["Command"]["CommandId"]})

    if "close_ports" in active_policy and active_policy["close_ports"]:
        resp = ssm_close_ports([instance_id], active_policy["close_ports"])
        actions.append({"action": "close_ports", "ports": active_policy["close_ports"], "command_id": resp["Command"]["CommandId"]})

    # Custom finding back to Security Hub
    if SECURITY_HUB_ENABLED:
        import_custom_finding(
            resource_arn=f"arn:aws:ec2:{REGION}:{boto3.client('sts').get_caller_identity()['Account']}:instance/{instance_id}",
            title=f"Auto-remediation for Config rule: {rule}",
            description=f"Remediation actions applied to {instance_id} due to non-compliance with {rule}.",
            severity="MEDIUM"
        )

    put_audit_log({"event": "config-noncompliance", "instance_id": instance_id, "rule": rule, "actions": actions, "tags": tags})
    notify("Config non-compliance remediated",
           f"Rule: {rule}\nInstance: {instance_id}\nActions: {actions}",
           "MEDIUM")
    return {"status": "ok", "actions": actions}

def handle_security_hub_finding(event):
    """
    EventBridge rule for Security Hub 'Finding Imported' or 'Severity >= ...'.
    Simple example: if finding indicates missing patches/open ports -> trigger SSM remediation.
    """
    detail = event.get("detail", {})
    findings = detail.get("findings", [])
    results = []

    for f in findings:
        resource_id = None
        for r in f.get("Resources", []):
            if r.get("Type") == "AwsEc2Instance":
                rid = r.get("Id", "")
                # rid may be full ARN or instance-id; normalize
                if ":instance/" in rid:
                    resource_id = rid.split(":instance/")[-1]
                else:
                    resource_id = rid
                break
        if not resource_id:
            continue

        tags = get_instance_tags(resource_id)
        if not is_in_scope(tags):
            continue

        title = f.get("Title", "").lower()
        desc  = f.get("Description", "").lower()
        actions = []

        if "patch" in title or "missing patch" in desc or "vulnerability" in desc:
            resp = ssm_run_patch([resource_id], "Install")
            actions.append({"action": "patch", "command_id": resp["Command"]["CommandId"]})

        if "open port" in title or "security group" in desc:
            resp = ssm_close_ports([resource_id], [22])  # example: always close SSH when flagged
            actions.append({"action": "close_ports", "ports": [22], "command_id": resp["Command"]["CommandId"]})

        put_audit_log({"event": "securityhub-finding", "finding_id": f.get("Id"), "instance_id": resource_id, "actions": actions})
        if actions:
            notify("Security Hub finding remediated",
                   f"Instance: {resource_id}\nFinding: {f.get('Title')}\nActions: {actions}",
                   "HIGH")
        results.append({"instance_id": resource_id, "actions": actions})

    return {"status": "ok", "results": results}

def handle_iot_device_defender(event):
    """
    EventBridge rule for AWS IoT Device Defender alarms/anomalies.
    This stub shows how you'd record and notify; remediation is device/app specific.
    """
    detail = event.get("detail", {})
    thing_name = detail.get("thingName") or detail.get("resourceId")
    anomaly = detail.get("behaviorName") or detail.get("alarmType", "Unknown")
    severity = detail.get("violationSeverity", "MEDIUM").upper()

    # Example: send command to edge via SSM if it's a managed EC2/Greengrass core,
    # or publish an IoT message to a topic for local agent to act.
    put_audit_log({"event": "iot-device-defender", "thing_name": thing_name, "anomaly": anomaly, "severity": severity})
    notify("IoT Device Defender alert",
           f"Thing: {thing_name}\nAnomaly: {anomaly}\nSeverity: {severity}",
           severity)
    return {"status": "ok", "thing": thing_name, "anomaly": anomaly}

# ---------------- Lambda Handler ----------------
def lambda_handler(event, context):
    """
    Entry: routes by source/pattern.
    Supported:
      - Scheduled scans (EventBridge: source='custom.deviceprotection', detail.action=Scan/Install)
      - AWS Config non-compliance (source='aws.config', detail.newEvaluationResult == 'NON_COMPLIANT')
      - Security Hub findings (source='aws.securityhub')
      - IoT Device Defender alarms (source='aws.iot')
    """
    logger.info(json.dumps({"event": event}))
    source = event.get("source", "")
    detail_type = event.get("detail-type", "")

    try:
        if source == "custom.deviceprotection":
            return handle_scheduled_scan(event)

        if source == "aws.config" and "Compliance Change" in detail_type:
            # Filter to NON_COMPLIANT only
            if event.get("detail", {}).get("newEvaluationResult", "") == "NON_COMPLIANT":
                return handle_config_rule_noncompliance(event)
            return {"status": "ignored", "reason": "Not non-compliant"}

        if source == "aws.securityhub":
            return handle_security_hub_finding(event)

        if source == "aws.iot":
            return handle_iot_device_defender(event)

        # Default: no route
        put_audit_log({"event": "unhandled", "detail_type": detail_type, "source": source})
        return {"status": "ignored", "reason": f"Unhandled source '{source}' / detail-type '{detail_type}'"}
    except Exception as e:
        put_audit_log({"event": "error", "error": str(e)})
        notify("Device Protection Lambda error", str(e), "CRITICAL")
        raise


# ---------------- Execution ----------------
 # lambda invokations