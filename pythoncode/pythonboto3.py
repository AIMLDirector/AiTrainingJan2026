import boto3
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

