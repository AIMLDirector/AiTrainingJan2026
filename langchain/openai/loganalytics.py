import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def analyze_log_entry(log_line: str):
    """Classifies a log entry as normal or an anomaly."""
    print(f"Analyzing: {log_line.strip()}")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an IT infrastructure monitoring assistant. Classify the user-provided server log line as 'NORMAL' or 'ANOMALY'. If ANOMALY, provide a 1-sentence reason."},
            {"role": "user", "content": f"Log line: {log_line}"}
        ],
        temperature=0, # Use low temperature for deterministic classification
        max_tokens=50
    )
    
    result = response.choices[0].message.content.strip()
    print(f"Classification: {result}\n")
    return result

# Simulate real-time inputs
log_stream_inputs = [
    "[INFO] User 'admin' logged in successfully from 192.168.1.1",
    "[WARN] Disk usage on /dev/sda1 is at 98%. System performance may degrade.",
    "[INFO] Scheduled backup completed in 4.2s.",
    "[CRITICAL] SSH login failed for root from 218.65.30.1. Possible brute force attempt."
]

for line in log_stream_inputs:
    analyze_log_entry(line)

