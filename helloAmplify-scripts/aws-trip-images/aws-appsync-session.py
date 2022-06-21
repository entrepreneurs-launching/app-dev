import boto3
import requests
from requests_aws4auth import AWS4Auth
import importlib
import logging
import datetime


# As found in AWS Appsync under Settings for your endpoint.
APPSYNC_API_ENDPOINT_URL = 'https://gv4gmbmdyfexrcxuwnxtvi7nuy.appsync-api.ap-south-1.amazonaws.com/graphql'
# Expires Fri, 16 Jun 2023 03:00:00 GMT
APPSYNC_API_KEY = 'da2-wvjkukzb6jfa7hiyyedz2jvfdq'
# Request Headers
headers = {
    'Content-Type': "application/graphql",
    'x-api-key': APPSYNC_API_KEY,
    'cache-control': "no-cache",
}


def sendRequest(json):
    response = session.request(
            url=APPSYNC_API_ENDPOINT_URL,
            method='POST',
            json=json,
            headers=headers
        )

    return response

def getAppsyncSession():
    # get credentials from ~/.aws
    # Use AWS4Auth to sign a requests session
    session = requests.Session()
    credentials = boto3.session.Session().get_credentials()
    session.auth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        boto3.session.Session().region_name,
        'appsync',
        session_token=credentials.token
    )
    
    return session

session = getAppsyncSession()
