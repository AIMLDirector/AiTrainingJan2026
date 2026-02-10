a = 5
b = 10

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")


if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a and b are equal")

import shutil
total, used, free  = shutil.disk_usage("/")
usage = used/total * 100 
print(usage)

if usage < 80:
    print("Disk usage is below 80%")
else:
    print("Disk usage is above 80%") 

import os 
serverip = [ "1.1.1.1", "8.8.8.8", "127.0.0.1"]
# Both for loop and if condition

for i in serverip:
    if os.system("ping -c 1 " + i) == 0:
        print(f"Server {i} is reachable")
    else:
        print(f"Server {i} is not reachable")

# what are the  ports open in my laptop  and check whether port 80 is open or not 
# check the cpu utilization of your system if cpu utilization is more than 80%  print warning message else print normal message

# # cloud - AWS
# # install  boto3 package in  your system using pip
# generate you access and secret key from aws console
# .env file - access and secret key 
# loadd the keys using load_dotenv function
# with for loop to list all the buckets in your account 
# boto3 module and  get the list of all the s3 buckets available in your account 

