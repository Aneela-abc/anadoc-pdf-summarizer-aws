# AnaDoc – PDF Summarizer using AWS Cloud

## 📌 Project Overview
AnaDoc is a **serverless cloud-based PDF document analyzer** that automatically extracts and summarizes text from uploaded PDF files using **AWS Free Tier services**.

The system uses **Amazon S3** for storage, **AWS Lambda** for processing, **IAM** for secure access control, and **CloudWatch** for monitoring. No servers or paid AI services are required.

---

## 🎯 Problem Statement
Manual analysis of long or multiple PDF documents is time-consuming and inefficient.  
There is a need for an automated, cost-effective solution that can summarize documents quickly using cloud computing without relying on paid AI APIs.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|----------|---------|
| Amazon S3 | Stores input PDFs and output summaries |
| AWS Lambda | Executes Python code automatically |
| AWS IAM | Role-based secure access |
| Amazon CloudWatch | Logging and monitoring |
| Python 3.11 | Programming language |
| PyPDF2 | Extracts text from PDF files |

---

## 🏗️ System Architecture & Workflow
1. User uploads a PDF file to the `input-files/` folder in an S3 bucket  
2. S3 upload event triggers the AWS Lambda function  
3. Lambda reads the PDF and extracts text using PyPDF2  
4. Extracted text is analyzed using a word-frequency based summarization algorithm  
5. A summary text file is generated  
6. The summary is stored in the `summaries/` folder in S3  
7. Execution logs are recorded in CloudWatch  

---

## ⚙️ AWS Setup Steps (Summary)

### Step 1: Create S3 Bucket
- Create an S3 bucket
- Add folders:
  - `input-files/`
  - `summaries/`

### Step 2: Create IAM Role
- Role Name: `LambdaS3AccessRole`
- Policies:
  - AmazonS3FullAccess
  - CloudWatchFullAccess

### Step 3: Create Lambda Function
- Function Name: `AnaDocLambda`
- Runtime: Python 3.11
- Execution Role: `LambdaS3AccessRole`
- Timeout: 1 minute

### Step 4: Upload Lambda Code
- Install dependencies (PyPDF2, boto3)
- Zip code and upload to Lambda
- Deploy the function

---

## 🧠 Summarization Logic
- Extracts text from all pages of the PDF
- Removes common stopwords
- Counts word frequency
- Selects top keywords
- Generates a concise summary based on most frequent terms

---

## 📂 Repository Structure
