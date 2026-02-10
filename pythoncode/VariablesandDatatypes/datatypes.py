#python Data types 
 # Text Data types: String (str)
 # Numeric Data types: Integer (int), Float (float), Complex (complex)
 # Sequence Data types: List (list), Tuple (tuple), Range (range)
 # Mapping Data type: Dictionary (dict) / json /yaml ( Name : kumar , age : 30 , city : hyd )
 # boolean Data type: Boolean (bool)  True / False or yes / no
 # Set Data type: Set (set)

#  Str, int, float, list, range , bool

#  import array
# import numpy as np # vectorization of storing the data

# range(start , stop, step )  range(0, 5, 1)  default start = 0 , step =1 

for i in range(10):   # 0  to 9 
    print(i) 


for i in range(5,200, 3):   # 5,7,9,...199 # 5,6,7.. 199
    print(i)

for i in range(3):   0,1,2
    system_check()

for i in range(1 8):  # last 7 days 
    delete_oldlog(i) # 1 to 7

for i in range(1,3):
    status = systemctl httpd status
    if status != "running":
        systemctl httpd start
        sleep(10)
    else:
        print("service is running fine")
        break








