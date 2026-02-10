
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.servicenow_tool import create_incident, update_incident

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

ticket_agent = initialize_agent(
    tools=[create_incident, update_incident],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)