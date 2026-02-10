# main.py
# from supervisor_agent import super_agent

# def monitor():
#     """
#     Orchestrate run and interpret output.
#     """
#     output = super_agent.run(
#         "Check Elasticsearch for CRITICAL logs, "
#         "if found provide remediation advice"
#     )
#     return output

# if __name__ == "__main__":
#     result = monitor()
#     print("\n====== ALERT RESPONSE ======\n")
#     print(result)

from supervisor_agent import super_agent

if __name__ == "__main__":
    result = super_agent()
    print("\n===== INCIDENT AUTOMATION RESULT =====\n")
    print(result)