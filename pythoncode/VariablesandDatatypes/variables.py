import os, sys


inpint_value = 1
print(inpint_value)  # to check the data type of variable
inpfloat_value = 1.5
print(inpfloat_value)
inpstr_value = "learning python"
print(inpstr_value)


def f1():
    inpintlocal_value = 10
    print("Inside function:", inpintlocal_value)


f1()

# print(inpintlocal_value)


def f2():
    pass
