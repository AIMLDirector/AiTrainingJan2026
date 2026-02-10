
import os
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
prompt = ChatPromptTemplate.from_template("Tell me a short fun fact about {topic}")
output_parser = StrOutputParser()

# The chain now converts the AI Message into a simple string
simple_string_chain = prompt | model | output_parser

topic_input = input("Enter a topic for a fun fact: ")
string_response = simple_string_chain.invoke({"topic": topic_input})

print(f"Topic: {topic_input}")
print("-" * 20)
# No need for .content, it's already a string
print(string_response)


# langchain, langchain-core , langchain-community, langchain-openai, pydantic, python-dotenv
# langchain-agents, langchain-tools(vendor), middleware ( vendor) - inmemory 
# chain -- input- prompt - model - output parser - output - serial method 
# chatopenai - model,temperature, max_tokens, streaming, api_key, top_p 