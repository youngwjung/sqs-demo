import boto3
import random
import string
import time
import requests

region = requests.get('http://169.254.169.254/latest/meta-data/placement/region').text

ssm = boto3.client('ssm', region_name=region)
resp = ssm.get_parameter(Name='week2_sqs_url')
SQS_URL=resp['Parameter']['Value']

sqs = boto3.resource('sqs', region_name=region)
queue = sqs.Queue(SQS_URL)

while True:
    message = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    queue.send_message(MessageBody=message)
    time.sleep(random.randrange(15))