import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

# 1. Define the desired output structure using Pydantic
class Fact(BaseModel):
    """Information about a topic."""
    fact: str = Field(description="A single interesting fact about the topic.")
    source: str = Field(description="The source of the fact, e.g., 'Wikipedia' or 'Annual Report'.")

class FactList(BaseModel):
    """A list of facts about a topic."""
    facts: list[Fact] = Field(description="A list of facts.")

# 2. Instantiate the Model (using a model that supports structured output, e.g., gpt-4o-mini)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert fact generator. Generate facts about the user's topic."),
    ("user", "{topic}")
])

# 4. Chain the components using the `.with_structured_output()` method
# This method handles the parsing internally, ensuring the output matches the schema
structured_chain = prompt | llm.with_structured_output(FactList)

# 5. Invoke the chain
topic = "The Planet Mars"
result_object = structured_chain.invoke({"topic": topic})

print(f"Topic: {topic}\n")
# The output is a validated Pydantic object (not just a raw string)
print(f"Type of result: {type(result_object)}")
for fact in result_object.facts:
    print(f"- Fact: {fact.fact}")
    print(f"  Source: {fact.source}")
