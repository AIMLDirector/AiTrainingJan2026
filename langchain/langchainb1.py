import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()
model = init_chat_model("gpt-4.1")

user_input = input("Enter you question : ")
response = model.invoke(user_input)

print(response.content)