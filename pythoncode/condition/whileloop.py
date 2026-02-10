import os,time

# while True:  # infinite loop
#     os.system("df -h")
#     time.sleep(10)

count = 0 
while count < 5:
    os.system("df -h")
    time.sleep(10)
    count += 1

# while True:  
#     os.system("ping -c 4 google.com")
#     time.sleep(5)
