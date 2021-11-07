"""Cam Hudson's Personal Website model (database) API.

Database is hosted by AWS DynamoDB. Tables include:
- database-dev
"""
from botocore.config import Config
from os import environ
import boto3
import flask
import camhudson

def get_db():
    if 'dynamodb' not in flask.g:
        db_client_config = Config(
            region_name='us-east-1',
            signature_version='v4',
            retries={
                'max_attempts': 5,
                'mode': 'standard'
            }
        )
        flask.g.dynamodb = boto3.client(
            'dynamodb',
            aws_access_key_id=environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=environ.get('AWS_SECRET_ACCESS_KEY'),
            config=db_client_config
        )

    return flask.g.dynamodb


@camhudson.app.teardown_appcontext
def close_db(error):
    """Close the database at the end of a request.

    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    flask.g.pop('dynamodb', None)
