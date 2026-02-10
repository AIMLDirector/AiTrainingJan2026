import os 

def disk_alert(usage, threshold=80):
    if usage > threshold:
        return "Alert: Disk usage is above threshold!"
    else:
        return "Disk usage is within acceptable limits."

def check_memory(memory_used, limit=70):
    if memory_used > limit:
        return "Warning: Memory usage exceeded limit!"
    else:
        return "Memory usage is normal."


def validate_ip(ip_address: str) -> bool:
    parts = ip_address.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True
