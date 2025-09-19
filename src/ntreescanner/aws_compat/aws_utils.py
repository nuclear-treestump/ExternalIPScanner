import requests
from src.ntreescanner.constants import SERVICES

def aws_get_regions(region_type):
    """
    Retrieves a list of AWS regions where a specified service is available.
    Args:
        region_type (str): The type of AWS service for which to retrieve regions. 
                           This should correspond to a key in the SERVICES dictionary.
    Returns:
        list: A list of region names (str) where the specified AWS service is available.
    Raises:
        KeyError: If the provided region_type is not found in the SERVICES dictionary.
        requests.exceptions.RequestException: If there is an issue with the HTTP request to the AWS regions API.
    """

    aws_regions = requests.get('https://api.regional-table.region-services.aws.a2z.com/index.json').json()["prices"]
    region_type = SERVICES[region_type]
    service_regions = []
    for region_obj in aws_regions:
        if region_obj["attributes"]["aws:serviceName"] == region_type:
            service_regions.append(region_obj["attributes"]['aws:region'])
    return service_regions
