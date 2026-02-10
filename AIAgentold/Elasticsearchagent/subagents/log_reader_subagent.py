# log_reader_subagent.py

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from log_reader_tool import fetch_critical_logs

log_reader_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

log_reader_subagent = initialize_agent(
    tools=[fetch_critical_logs],
    llm=log_reader_llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=False
)