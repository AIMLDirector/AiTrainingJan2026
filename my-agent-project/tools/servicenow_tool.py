import requests
from requests.auth import HTTPBasicAuth
from langchain.tools import tool

SN_INSTANCE = "pythonm"
SN_USER = "YOUR_USERNAME"
SN_PASS = "YOUR_PASSWORD"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

@tool
def create_incident(short_description: str, description: str) -> str:
    """
    Create ServiceNow incident
    """
    url = f"{SN_INSTANCE}/api/now/table/incident"

    payload = {
        "short_description": short_description,
        "description": description,
        "urgency": "1",
        "impact": "2",
        "category": "infrastructure"
    }

    r = requests.post(
        url,
        auth=HTTPBasicAuth(SN_USER, SN_PASS),
        headers=HEADERS,
        json=payload
    )

    r.raise_for_status()
    result = r.json()["result"]
    return f"{result['number']}::{result['sys_id']}"

@tool
def update_incident(sys_id: str, suggestion: str) -> str:
    """
    Update ServiceNow incident with AI suggestion
    """
    url = f"{SN_INSTANCE}/api/now/table/incident/{sys_id}"

    payload = {
        "work_notes": suggestion
    }

    r = requests.patch(
        url,
        auth=HTTPBasicAuth(SN_USER, SN_PASS),
        headers=HEADERS,
        json=payload
    )

    r.raise_for_status()
    return "Incident updated with suggestion"