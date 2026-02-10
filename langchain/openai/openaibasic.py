import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv() # Load environment variables if using a .env file

AI = OpenAI()

response = AI.chat.completions.create(
    model="gpt-3.5-turbo", # Use an existing model name
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ],
    max_tokens=100 # plus or minus based on your needs ( 150 word )
)

story_text = response.choices[0].message.content

print(story_text)
