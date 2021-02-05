import boto3
import random
import time

ssm = boto3.client('ssm')
resp = ssm.get_parameter(Name='week2_sqs_url')
SQS_URL=resp['Parameter']['Value']

sqs = boto3.resource('sqs')
queue = sqs.Queue(SQS_URL)

while True:
    for message in queue.receive_messages(VisibilityTimeout=60):
        print (f'{message.body}')
        message.delete()
        time.sleep(random.randrange(30))