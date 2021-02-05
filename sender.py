import boto3
import random
import string
import time

ssm = boto3.client('ssm')
resp = ssm.get_parameter(Name='week2_sqs_url')
SQS_URL=resp['Parameter']['Value']

sqs = boto3.resource('sqs')
queue = sqs.Queue(SQS_URL)

while True:
    message = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    queue.send_message(MessageBody=message)
    time.sleep(random.randrange(15))