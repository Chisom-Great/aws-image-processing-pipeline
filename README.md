# Image Recognition Pipeline with AWS

![AWS Logo](https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg)

## Project Overview
This project demonstrates a fully serverless image recognition workflow using AWS services. Users can upload images through a simple web interface, and the images are automatically processed using AWS Lambda and Amazon Rekognition. The results are saved in JSON format in an S3 bucket.

**Key Skills Demonstrated:**
- AWS S3 bucket management & permissions
- Serverless computing with AWS Lambda
- API Gateway for presigned URL uploads
- Amazon Rekognition for image analysis
- Frontend integration (HTML + JavaScript)
- CORS configuration & secure file upload

---

## Architecture

[User Browser]
|
[upload.html] --(select file)--> [API Gateway] --(presigned URL)--> [S3 Input Bucket]
|
Trigger Lambda (great-image-processor)
|
[Amazon Rekognition] --> [S3 Output Bucket]
![Architecture Diagram](screenshots/architecture-diagram.png)

---

## Implementation Steps

### 1. Create S3 Buckets
- **Input Bucket:** `great-input-bucket` – stores uploaded images  
- **Output Bucket:** `great-output-bucket` – stores JSON results  

### 2. Configure S3

**CORS configuration** for input bucket:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]
Bucket policy for presigned URL uploads:{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPresignedUpload",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:PutObject","s3:PutObjectAcl"],
      "Resource": "arn:aws:s3:::great-input-bucket/*"
    }
  ]
}
Lambda Functionslambda-get-presigned-url.py – Generates presigned URLs for secure uploads.

lambda-image-processor.py – Triggered by S3 uploads, uses Amazon Rekognition to detect labels, and saves results as JSON in the output bucket.
Frontend Integration

frontend/upload.html – Simple HTML + JS page to upload images.Testing Steps:

Open upload.html in the browser.

Select an image and click Upload.

Verify the image appears in great-input-bucket.

Wait a few seconds and check great-output-bucket for JSON results:Cost Considerations

S3: Charged per GB stored.

Lambda: Charged per execution duration and memory.

Amazon Rekognition: Charged per image processed.

Tip: Delete test images after completion to reduce costs.Possible Improvements

Store results in DynamoDB for easy querying.

Create a frontend viewer to display labels visually.

Use Rekognition Custom Labels for specialized detection.

Add authentication & access control.

Generate automatic thumbnails in the output bucket

