import boto3

from ntreescanner.config import *

def get_auth_session(region_str = None) -> boto3.Session:
    """
    Generates auth session for the given region_str using the configured AWS_SECRET_ACCOUNT.

    Parameters:
        region_str (str): AWS region string

    Returns:
        boto3.Session: Boto3 session object
    """
    role = AWS_SECRET_ACCOUNT["role_name"]
    account_id = AWS_SECRET_ACCOUNT["account_num"]

    if AWS_SECRET_ACCOUNT["auth_type"] == "env":
        if region_str is not None:
            session = boto3.Session(
                aws_access_key_id=AWS_SECRET_ACCOUNT["access_key_id"],
                aws_secret_access_key=AWS_SECRET_ACCOUNT["secret_access_key"],
                region_name=region_str
            )
            return session
        else:
            session = boto3.Session(
                aws_access_key_id=AWS_SECRET_ACCOUNT["access_key_id"],
                aws_secret_access_key=AWS_SECRET_ACCOUNT["secret_access_key"]
            )
            return session
    elif AWS_SECRET_ACCOUNT["auth_type"] == "profile":
        if region_str is not None:
            session = boto3.Session(profile_name=f"{role}-{account_id}", region_name=region_str)
            return session
        else:
            session = boto3.Session(profile_name=f"{role}-{account_id}")
            return session


def get_secret(secret_name: str, region_str: str) -> dict|None|str:
    """
    Get secret from AWS Secrets Manager for the given secret_name and region_str

    Parameters:
        secret_name (str): AWS secret name
        region_str (str): AWS region string
    Returns:
        dict|str|None: Secret value as a dictionary, string, or None if not found 
    """
    region = region_str if region_str is not None else AWS_SECRET_ACCOUNT["region"]

    if AWS_SECRET_ACCOUNT["auth_type"] == "env":
        session = boto3.Session(
            aws_access_key_id=AWS_SECRET_ACCOUNT["access_key_id"],
            aws_secret_access_key=AWS_SECRET_ACCOUNT["secret_access_key"],
            region_name=region
        )
        client = session.client('secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return secret
    elif AWS_SECRET_ACCOUNT["auth_type"] == "profile":
        session = get_auth_session(region)
        client = session.client('secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return secret
    raise RuntimeError("Unsupported AWS auth_type configured.")