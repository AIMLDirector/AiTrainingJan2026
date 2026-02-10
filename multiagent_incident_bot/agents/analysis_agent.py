from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

analysis_executor = create_agent(
    model=llm,              # Renamed from llm
    tools=[],               # Empty list OK for analysis-only
    system_prompt="""You are an SRE expert.

Analyze the logs and provide:
1. Root cause
2. Affected service  
3. Severity
4. Business impact""",  # String (no PromptTemplate)
)

# Invoke with messages dict
logs = "your actual log content here"  # Replace with real logs

result = analysis_executor.invoke({
    "messages": [HumanMessage(content=logs)]  # Input goes in messages
})
print(result["messages"][-1].content)  # Final analysis