import os
from dotenv import load_dotenv
# Import BaseModel and Field directly from the pydantic library
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# 1. Define the desired output structure using Pydantic
class ContactInfo(BaseModel):
    """
    Structured information about a person's contact details.
    """
    name: str = Field(description="The full name of the person.")
    phone_number: str = Field(description="Their primary phone number")
    email_address: str = Field(description="Their primary email address.")
    
    # You can add validation logic right in the Pydantic model if needed
    # @field_validator('email_address')
    # def check_email_format(cls, v):
    #     if "@" not in v:
    #         raise ValueError("Email must contain an @ symbol")
    #     return v

# 2. Instantiate the Model
# Use a model known for reliable function calling/structured output (like gpt-4o-mini)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract the requested contact information from the following text."),
    ("user", "{text_input}")
])

# 4. Chain the components using the `.with_structured_output()` method
# This method tells the LLM to return data matching the ContactInfo schema
extraction_chain = prompt | llm.with_structured_output(ContactInfo)

# 5. Invoke the chain
input_text = """
Contact for the project is John Doe. 
You can reach him at 555-123-4567. 
He prefers email communication at john.doe@example.com.
"""
result_object = extraction_chain.invoke({"text_input": input_text})

# 6. Use the validated Pydantic object
print(f"Input Text Analyzed:\n{input_text}")
print("-" * 40)
# print(f"Type of result: {type(result_object)}")
print(f"Name:         {result_object.name}")
print(f"Phone Number: {result_object.phone_number}")
print(f"Email:        {result_object.email_address}")
