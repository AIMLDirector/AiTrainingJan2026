import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file (optional)
load_dotenv()

# 1. Instantiate the Model
# Ensure OPENAI_API_KEY is set in your environment
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=200, streaming=True)

# 2. Define the Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to French, Your primary objective is to answer questions accurately without compromising user privacy"),
    ("user", "{question}")
])

# 3. Define the Output Parser
# This simple parser turns the AI Message output into a string
output_parser = StrOutputParser()

# 4. Chain the components using LCEL (| operator)
# The output of the prompt goes to the model, and the output of the model goes to the parser
chain = prompt | model | output_parser

# 5. Invoke the chain
question = "I love programming in Python."
response = chain.invoke({"question": question})

print(f"Original English: {question}")
print(f"French Translation: {response}")

# You can also stream the response
print("\nStreaming response:")
for chunk in chain.stream({"question": "How do you build a website?"}):
    print(chunk, end="", flush=True)
