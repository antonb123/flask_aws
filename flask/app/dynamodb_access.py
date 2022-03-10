import os
import datetime
import boto3


def get_resource():
    return boto3.resource('dynamodb',
                          aws_access_key_id=os.environ['AWS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
                          region_name='eu-north-1')


def get_all_readings():
    client = get_resource()
    table = client.Table('water_temperature')
    response = table.scan()
    responses = response['Items']
    for response in responses:
        response['datetime'] = datetime.datetime.strptime(response['datetime'], "%Y-%m-%d %H:%M:%S")
    responses.sort(key=lambda item: item['datetime'], reverse=True)
    return responses