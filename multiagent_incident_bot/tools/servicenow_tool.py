import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("SN_INSTANCE")
AUTH = HTTPBasicAuth(
    os.getenv("SN_USER"),
    os.getenv("SN_PASSWORD")
)
HEADERS = {"Content-Type": "application/json"}


def create_incident(short_desc, description):
    url = f"{BASE_URL}/api/now/table/incident"

    payload = {
        "short_description": short_desc,
        "description": description,
        "urgency": "1",
        "impact": "1"
    }

    response = requests.post(url, auth=AUTH, headers=HEADERS, json=payload)
    response.raise_for_status()

    result = response.json()["result"]
    print(result)
    # return {
    #     "number": result["number"],
    #     "sys_id": result["sys_id"]
    # }


def update_incident(sys_id, work_notes):
    url = f"{BASE_URL}/api/now/table/incident/{sys_id}"
    payload = {"work_notes": work_notes}
    response = requests.patch(url, auth=AUTH, headers=HEADERS, json=payload)
    response.raise_for_status()
    print(response.json())
    #return "updated"

# create_incident(
#     "Test Incident from AI",
#     "This is a test incident created by the AI tool integration."
# )


update_incident(
    "sys_id_here",
    "Adding work notes to the incident via AI tool integration."
)