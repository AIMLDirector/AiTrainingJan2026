import json
from agents.elastic_agent import elastic_tool
from agents.analysis_agent import analysis_executor
from agents.recommendation_agent import recommend_executor
from agents.servicenow_agent import create_ticket_tool, update_ticket_tool


def run_pipeline():
    
    logs_result = elastic_tool.invoke({})
    print(logs_result)

    if not logs_result:
        return "No critical logs found."

    # 2️⃣ Normalize logs → STRING ONLY
    logs = []
    for hit in logs_result:
        if isinstance(hit, dict):
            logs.append(hit.get("message") or json.dumps(hit))
        else:
            logs.append(str(hit))

    logs_text = "\n".join(logs)
    
    

    print(f"Analyzing logs:\n{logs_text[:200]}...")

    # 3️⃣ Analysis agent (STRING INPUT)
    analysis_result = analysis_executor.invoke({
        "input": logs_result
    })
    analysis = analysis_result.get("final_output") or analysis_result.get("output")
    print(f"Analysis Result:\n{analysis}")

    # 4️⃣ Create ServiceNow ticket
    incident = create_ticket_tool.invoke({
        "short_desc": "Critical Incident detected via Elasticsearch",
         "description": f"""
Analysis:
{analysis}

Raw Logs:
{logs_text}
"""
    })

    # 5️⃣ Recommendation agent (STRING INPUT)
    rec_result = recommend_executor.invoke({
        "input": analysis
    })
    solution = rec_result["output"]

    # 6️⃣ Update same ticket
    update_ticket_tool.invoke({
        "sys_id": incident["sys_id"],
        "work_notes": f"""
🤖 AI Suggested Solution:

{solution}

⚠️ Review before implementation.
"""
    })

    return f"""
Incident Created: {incident.get("number", "N/A")}
🛠 Solution added to work notes
"""