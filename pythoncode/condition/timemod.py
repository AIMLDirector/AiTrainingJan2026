import time
import os
print("current time:", time.time())  

print("current time:", time.ctime(time.time()))
print(time.localtime())

# start = time.time()
# time.sleep(10)
# end = time.time()
# print("Elapsed time:", end - start)
print("Formatted time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print("Formatted time:", time.strftime("%d.%m.%Y %H:%M", time.localtime()))

timestamp = time.strftime("%d_%m_%Y_%H_%M", time.localtime())
os.mkdir(f"applicationlog_{timestamp}") if not os.path.exists(f"applicationlog_{timestamp}") else None