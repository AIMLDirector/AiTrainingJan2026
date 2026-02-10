try:
    print("Checking disk alert for 85% usage:")
except:
    Print("An error occurred while printing disk alert message.")


try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found. Please check the file path.")


try:
    print("Checking disk alert for 85% usage:")
except:
    Print("An error occurred while printing disk alert message.")
else:
    print("Disk alert message printed successfully.")
finally:
    print("Finished attempting to print disk alert message.")