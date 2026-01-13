import json
import boto3
import PyPDF2
import re
from collections import Counter

s3 = boto3.client('s3')

STOPWORDS = set([
    'the','is','and','to','of','in','that','it','on','for','with',
    'as','was','were','this','by','are','from'
])

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    if not key.endswith('.pdf'):
        return {'statusCode': 400, 'body': 'Not a PDF file'}

    response = s3.get_object(Bucket=bucket, Key=key)
    pdf_reader = PyPDF2.PdfReader(response['Body'])

    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    keywords = [w for w in words if w not in STOPWORDS]

    freq = Counter(keywords).most_common(10)

    summary = "Top Keywords Summary:\n\n"
    for word, count in freq:
        summary += f"{word} : {count}\n"

    output_key = key.replace("input-files/", "summaries/").replace(".pdf", ".txt")

    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=summary.encode('utf-8')
    )

    return {
        'statusCode': 200,
        'body': 'Summary created successfully!'
    }
