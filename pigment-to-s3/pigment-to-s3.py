# -*- coding: utf-8 -*-
"""Example AWS Lambda Function to Export Pigment Block data to an S3 Bucket.

@Author: Guini
@License: MIT
@Links: https://github.com/Guini/PigmentSamples

"""

from datetime import datetime
import os
import json
import boto3
import requests
from botocore.exceptions import ClientError

# Init AWS Secrets Manager
def get_secret():

    # Replace with your AWS secrets manager details via the environment variables
    SECRET_NAME = os.environ['AWS_SECRET_NAME']
    REGION_NAME = os.environ['AWS_SECRET_REGION']
    SECRET_KEY = os.environ['SECRET_KEY']

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=REGION_NAME
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=SECRET_NAME
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret_response = get_secret_value_response['SecretString']
    secret_dict = json.loads(secret_response)
    return secret_dict[SECRET_KEY]

# Replace with your S3 Bucket name and desired S3 name (object name)
# Adding a folder for each export attempt, feel free to remove if overkill
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
DT = datetime.now()
DT_ISO = DT.strftime("%Y-%m-%dT%H:%M:%SZ")
S3_FILE = f'pigment_exports/{DT_ISO}/export.csv'

def lambda_handler(event, context):
    # Yor Pigment block's App ID and View ID
    APP_ID = os.environ['APP_ID']
    VIEW_ID = os.environ['VIEW_ID']

    # Compose export API URI
    API_URL = f'https://pigment.app/api/workspace/{APP_ID}/view/ExportListData/{VIEW_ID}'  
    KEY = get_secret()
    HEADERS = {'X-Pigment-Api-Key': KEY}
    
    # Initialize S3 client
    s3 = boto3.client('s3')

    try:
        # Make the HTTP GET request to the API
        response = requests.get(API_URL, headers=HEADERS)

        if response.status_code == 200:
            # Save the content to S3
            s3.put_object(Bucket=S3_BUCKET_NAME, Key=S3_FILE, Body=response.content)
            return {
                'statusCode': 200,
                'body': json.dumps('File saved to S3 successfully!')
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps('Failed to retrieve data from the API.')
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }