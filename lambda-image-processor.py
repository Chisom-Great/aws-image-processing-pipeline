import json
import boto3

s3 = boto3.client('s3')
rek = boto3.client('rekognition')

OUTPUT_BUCKET = "great-output-bucket"   # stay exactly like this

def lambda_handler(event, context):
    print("Event:", event)

    bucket = event['Records'][0]['s3']['bucket']['name']
    key    = event['Records'][0]['s3']['object']['key']

    response = rek.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=10
    )

    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=key + ".json",
        Body=json.dumps(response)
    )

    return {
        "statusCode": 200,
        "body": "Analysis done!"
    }
