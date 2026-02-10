def func1():
    print("This is func1")


func1()
func1()
func1()

def func2(a,b):
    sum = a + b
    return sum

value1 = func2(10,20)
print("Sum is:", value1)



def func3(a:int=10, b:int=20) -> int:
    sum = a + b
    return sum


value2 = func3()
print("Sum of values:", value2)
value2 = func3(30,50)
print("Sum of values:", value2)


def disk_alert(usage, threshold=80):
    if usage > threshold:
        return "Alert: Disk usage is above threshold!"
    else:
        return "Disk usage is within acceptable limits."

result1 = disk_alert(85)
print(result1)
result2 = disk_alert(80, 65)
print(result2)

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

    
