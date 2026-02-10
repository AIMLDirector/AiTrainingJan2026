import os 



print(os.getcwd())

os.chdir("/var/tmp/")

os.mkdir("test_dir") if not os.path.exists("test_dir") else "Directory already exists"   # one-liner if-else
# print("Directory created" if os.path.exists("test_dir") else "Directory already exists")
os.rmdir("test_dir") if os.path.exists("test_dir") else None

os.rmdir("testdir1") if os.path.exists("testdir1") else None

# if not os.path.exists("test_dir"):
#     os.mkdir("test_dir")
#     print("Directory created")
# else:
#     print("Directory already exists")  
# print(os.listdir("/var/log"))
# print(os.getenv("ENV"))

is_production = True if os.getenv("ENV") == "PRODUTION" else False
if is_production:
    print("Running in production mode")
    os.system("df -h")
else:
    print("Running in development mode")
    os.system("ls -l") 
   

