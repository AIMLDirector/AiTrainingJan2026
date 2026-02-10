import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (optional, assuming key is set elsewhere)
load_dotenv() 

# 1. Instantiate the Model
# We use a reliable, fast model
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=150)

# 2. Define a Simple Prompt Template
# The template takes an input variable named "topic"
prompt = ChatPromptTemplate.from_template(
    "Tell me a short fun fact about {topic}"
)

# 3. Chain the prompt and the model using LCEL (the pipe operator)
# This creates a single, simple chain
chain = prompt | model

# 4. Invoke the chain with input data
topic_input = input("Enter a topic for a fun fact: ")
response = chain.invoke({"topic": topic_input})

# 5. Print the output
# The output is an 'AIMessage' object, so we access its content attribute
print(f"Topic: {topic_input}")
print("-" * 20)
print(response.content)
print("-" * 20)
print(response)
print("-" * 20)