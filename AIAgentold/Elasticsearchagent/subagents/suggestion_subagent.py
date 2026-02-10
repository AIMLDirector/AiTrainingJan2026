# suggestion_subagent.py
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

suggestion_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

suggestion_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an SRE expert who analyzes critical system logs."),
    ("human", "Logs:\n{logs}\n\n"
              "Provide:\n"
              "1) Likely cause\n"
              "2) Immediate action\n"
              "3) Preventive steps")
])

suggestion_subagent = LLMChain(
    llm=suggestion_llm,
    prompt=suggestion_prompt
)