import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
client = OpenAI()

# 1. Define the desired output structure using Pydantic with default values/options
class SecurityAlert(BaseModel):
    """Details of a detected security event."""
    ip_address: str = Field(description="The source IP address of the potential threat.")
    # Add an explicit list of possible values to constrain the AI's output
    threat_level: str = Field(description="Severity of the threat: LOW, MEDIUM, HIGH, or CRITICAL.")
    description: str = Field(description="A brief explanation of the threat detected.")
    action_required: bool = Field(description="True if human intervention or automated blocking is recommended.")

# Generate the JSON schema string once
alert_schema_json = SecurityAlert.model_json_schema()

def process_security_alert(raw_log):
    # Ensure the system prompt is extremely directive
    system_prompt = f"""
    You are an expert security analyst assistant. Your task is to extract information 
    from the provided raw log entry and format it *only* as a strict JSON object.
    You MUST adhere precisely to the following JSON schema. Do not output anything 
    other than the JSON object itself.

    Schema:
    {alert_schema_json}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Using gpt-4o-mini often improves structured output reliability
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": raw_log}
        ],
        response_format={"type": "json_object"} 
    )

    json_string = response.choices[0].message.content
    
    # Clean the string of markdown wrappers if the model includes them
    if json_string.strip().startswith("```json"):
        json_string = json_string.strip("```json").strip("```").strip()
    
    try:
        # We parse the clean JSON string into our Pydantic object
        alert_object = SecurityAlert.model_validate_json(json_string)
        
        print(f"--- Processed Security Alert Object ---")
        print(f"Source IP:      {alert_object.ip_address}")
        print(f"Threat Level:   {alert_object.threat_level}")
        print(f"Action Req:     {alert_object.action_required}")
        print(f"Description:    {alert_object.description}")
        
    except Exception as e:
        print(f"Pydantic validation failed. This usually means the AI returned bad JSON.")
        print(f"Error: {e}")
        print(f"Raw response was:\n{json_string}")


raw_input_log = "Alert: High volume of traffic detected from 10.0.0.44 attempting to access port 22 (SSH) with invalid credentials."
process_security_alert(raw_input_log)
