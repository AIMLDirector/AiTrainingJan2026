import os
from dotenv import (
    load_dotenv,
)  # environment variables from .env file will be loaded using python-dotenv packages

load_dotenv()
api_key = os.getenv("API_KEY")

a = 10

if a > 5:
    print("a is greater than 5")
