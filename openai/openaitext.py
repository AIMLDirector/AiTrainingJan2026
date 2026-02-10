from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
print("OpenAI API Key set successfully.")

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

