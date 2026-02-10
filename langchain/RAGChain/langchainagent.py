import os
from langchain.agents import create_agent
# from langchain.tools import tool, TravilySearch
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
travily_tool = TavilySearch(max_results=3, api_key=os.getenv("TRAVILY_API_KEY"))
tools = [travily_tool]

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3, api_key=os.getenv("OPENAI_API_KEY"))

agent = create_agent(model, tools,
system_prompt="you are a helpful assistant that uses the Travily web search tool to answer user queries based on up-to-date web information.")

query = "What are the latest advancements in renewable energy technologies?"
inputs = {"messages": [{"role": "user", "content": query}]}
response = agent.invoke(inputs)

print(response["messages"][-1].content)
