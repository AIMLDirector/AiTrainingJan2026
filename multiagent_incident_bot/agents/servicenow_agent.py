from langchain_core.tools import StructuredTool
from tools.servicenow_tool import create_incident, update_incident

create_ticket_tool = StructuredTool.from_function(
    name="create_servicenow_incident",
    func=create_incident,
    description="Create a ServiceNow incident"
)

update_ticket_tool = StructuredTool.from_function(
    name="update_servicenow_incident",
    func=update_incident,
    description="Update ServiceNow incident with work notes"
)