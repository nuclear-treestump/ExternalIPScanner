

# AWS Secrets Retrieval Role Configuration
# These values should be set according to your AWS environment.
# Required for AWS secret retrieval.
# If using AWS STS, set AWS_SECRET_SUPPORT_STS to True and ensure your AWS CLI is configured for role assumption.
# Otherwise the code will be sad.


# This gets overwritten later during config assertion.
AWS_SECRET_SESSION_NAME = ""
AWS_SECRET_SESSION_ROLE = ""
AWS_SECRET_SESSION_ACCOUNTNUM = ""
AWS_SECRET_SUPPORT_STS = False
AWS_SECRET_STS_DURATION = 3600  # Duration in seconds for the STS session
AWS_SECRET_PERMIT_WRITE = False  # Set to True to allow write operations, False for read-only
AWS_SECRET_REGION = "us-east-1"  # Default region for AWS Secrets Manager operations
AWS_SECRET_ACCESS_KEY_ID = ""
AWS_SECRET_SECRET_ACCESS_KEY = ""
AWS_AUTH_TYPE = ""  # Options: "profile" or "env"

import os
import json

try:
    configpath = os.getenv("NTREESCANNER_CONFIG_PATH", "ntreescanner.config")
    with open(configpath, "r") as f:
        config_data = json.load(f)
        aws_secrets_read = config_data.get("secrets_read", {})
except FileNotFoundError:
    print("No ntreescanner.config file found, proceeding with second level configuration options.")
    config_data = {}
    aws_secrets_read = {}

if not aws_secrets_read:
    AWS_SECRET_SESSION_NAME = os.getenv("AWS_SECRET_SESSION_NAME", "")
    AWS_SECRET_SESSION_ROLE = os.getenv("AWS_SECRET_SESSION_ROLE", "")
    AWS_SECRET_SESSION_ACCOUNTNUM = os.getenv("AWS_SECRET_SESSION_ACCOUNTNUM", "")
    AWS_SECRET_SUPPORT_STS = os.getenv("AWS_SECRET_SUPPORT_STS", "False").lower() == "true"
    AWS_SECRET_STS_DURATION = int(os.getenv("AWS_SECRET_STS_DURATION", "3600"))  # Duration in seconds for the STS session token
    AWS_SECRET_PERMIT_WRITE = os.getenv("AWS_SECRET_PERMIT_WRITE", "False").lower() == "true"  # Set to True to allow write operations, False for read-only
    AWS_SECRET_REGION = os.getenv("AWS_SECRET_REGION", "us-east-1")  # Default region for AWS Secrets Manager operations
    AWS_SECRET_ACCESS_KEY_ID = os.getenv("AWS_SECRET_ACCESS_KEY_ID", "")
    AWS_SECRET_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_SECRET_ACCESS_KEY", "")
    # This is important for determining how to authenticate with AWS.
    # This will first try to use the AWS profile named in the format {role}-{account_id}
    # If that fails, it will then try to retrieve credentials from the following ENV variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    # If you don't want to use profiles, set this to "env"
    AWS_AUTH_TYPE = os.getenv("AWS_AUTH_TYPE", "env").lower()  # Options: "profile" or "env"

AWS_SECRET_ACCOUNT = {
    "softname": "AWS_SECRET_AUTH", # This is a label used inside the software to identify this configuration. Do not change this.
    "account_num": (AWS_SECRET_SESSION_ACCOUNTNUM or aws_secrets_read.get("account_num", "")),
    "role_name": (AWS_SECRET_SESSION_ROLE or aws_secrets_read.get("role_name", "")),
    "region": (AWS_SECRET_REGION or aws_secrets_read.get("region", "")),
    "sts_config" : {
        "support_sts": (AWS_SECRET_SUPPORT_STS or aws_secrets_read.get("support_sts", False)),
        "sts_duration": (AWS_SECRET_STS_DURATION or aws_secrets_read.get("sts_duration", 3600))  # Duration in seconds for the STS session token
    },
    "permit_write": (AWS_SECRET_PERMIT_WRITE or aws_secrets_read.get("permit_write", False)),
    "auth_type": (AWS_AUTH_TYPE or aws_secrets_read.get("auth_type", "env")),
    "access_key_id": (AWS_SECRET_ACCESS_KEY_ID or aws_secrets_read.get("access_key_id", "")),
    "secret_access_key": (AWS_SECRET_SECRET_ACCESS_KEY or aws_secrets_read.get("secret_access_key", ""))
}

