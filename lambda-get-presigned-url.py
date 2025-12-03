import boto3
import json

s3 = boto3.client('s3')
BUCKET = "great-input-bucket"  # replace with your input bucket name

def lambda_handler(event, context):
    # Get the filename from the browser request
    filename = event['queryStringParameters']['filename']
    
    # Generate pre-signed PUT URL valid for 1 hour
    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={'Bucket': BUCKET, 'Key': filename},
        ExpiresIn=3600
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # allows browser access
        },
        'body': json.dumps({'url': url})
    }
