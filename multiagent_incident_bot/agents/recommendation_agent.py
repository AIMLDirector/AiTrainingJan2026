from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

recommend_executor = create_agent(
    model=llm,                           # Changed: llm → model
    tools=[],                            # No tools needed for pure analysis
    system_prompt="""You are a senior DevOps engineer.

Based on the incident analysis, suggest:
- Immediate remediation
- Long-term fix  
- Monitoring improvements""",          # Changed: PromptTemplate → string
)

# Usage in pipeline:
analysis = "your analysis text here"
result = recommend_executor.invoke({
    "messages": [HumanMessage(content=analysis)]  # Input format
})
recommendation = result["messages"][-1].content  # Extract final output