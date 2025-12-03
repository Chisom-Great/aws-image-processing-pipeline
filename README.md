![](https://via.placeholder.com/1000x250/000000/ffffff?text=AWS+Image+Recognition+Pipeline+%7C+Serverless+Rekognition+Project)

# 🖼️ AWS Image Recognition Pipeline

A fully serverless image-processing workflow built using **AWS S3, Lambda, Rekognition, and API Gateway**.  
Users upload an image via a simple frontend, AWS processes it automatically, and the system returns a JSON output of detected objects.

---

## 🚀 Features
- Automated image processing using **AWS Lambda**
- Image recognition powered by **Amazon Rekognition**
- Frontend upload via **presigned URL**
- Secure, scalable & fully serverless architecture
- Result stored as JSON inside S3 output bucket

---

## 🧩 System Architecture

[ User Browser ]
|
v
upload.html → API Gateway → S3 (Input Bucket)
|
v
Trigger Lambda (great-image-processor)
|
v
Amazon Rekognition → S3 (Output Bucket with JSON result)
---

## 🔧 Implementation Steps

### 1️⃣ Create S3 Buckets
| Bucket | Purpose |
|-------|----------|
| `great-input-bucket` | Stores uploaded images |
| `great-output-bucket` | Stores JSON recognition results |

---

### 2️⃣ Configure Input Bucket (CORS + Policy)

#### **CORS**
```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "HEAD"],
    "AllowedOrigins": ["*"]
  }
]
Bucket Policy{
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
How to Test

Open upload.html

Select an image → click Upload

Check great-input-bucket for image

Check great-output-bucket for result JSON

(Optional) View logs inside CloudWatch{
  "Labels": [
    {"Name": "Person", "Confidence": 99.0},
    {"Name": "Car", "Confidence": 87.5}
  ]
}
Cost Notes
Service	Charge
S3	Storage usage
Lambda	Execution time
Rekognition	Per image processed

Delete test images to reduce cost.Future Improvements

Store results in DynamoDB

Build UI to display label results visually

Rekognition Custom Labels (custom training)

Add authentication user access control

aws-image-processing-pipeline
