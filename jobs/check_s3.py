import boto3
import sys

BUCKET_NAME = "s3://prithiv-ecommerce-raw-751835847273/"
PREFIX = "raw/"

s3 = boto3.client("s3")

response = s3.list_objects_v2(
    Bucket=BUCKET_NAME,
    Prefix=PREFIX
)

files = response.get("Contents", [])

if not files:
    print("No files found in S3 raw folder.")
    sys.exit(1)

print(f"Found {len(files)} file(s) in s3://{BUCKET_NAME}/{PREFIX}")