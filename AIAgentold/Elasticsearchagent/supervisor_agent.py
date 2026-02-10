from subagents.log_reader_subagent import log_reader_subagent
from subagents.suggestion_subagent import suggestion_subagent
from subagents.ticket_agent import ticket_agent
from tools.servicenow_tool import create_incident, update_incident


def super_agent():
    # Step 1: Read CRITICAL logs
    logs = log_reader_subagent.run("Fetch CRITICAL logs")

    if not logs or "NO_CRITICAL_ALERTS" in str(logs):
        return "✅ No critical alerts"

    # Step 2: Generate suggestion
    suggestion = suggestion_subagent.run(logs=logs)

    # Step 3: Create incident (DIRECT tool call – safer)
    create_result = create_incident(
        short_description="Critical Alert from Elasticsearch",
        description=logs
    )

    # create_result format: INC001234::sys_id
    try:
        incident_number, sys_id = create_result.split("::")
    except ValueError:
        raise RuntimeError(f"Unexpected ServiceNow response: {create_result}")

    # Step 4: Update incident with suggestion
    update_incident(
        sys_id=sys_id,
        suggestion=suggestion
    )

    return {
        "incident": incident_number,
        "sys_id": sys_id,
        "suggestion": suggestion
    }