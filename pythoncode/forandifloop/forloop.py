# for i in range(1, 5):
#     if i %2  == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# oddnumber = []
# evennumber = []

# for i in range(1, 5):
#     if i %2  == 0:
#         print(f"{i} is even")
#         evennumber.append(i)
#     else:
#         print(f"{i} is odd")
#         oddnumber.append(i)

# print("Odd numbers:", oddnumber)
# print("Even numbers:", evennumber)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# oddnumber = []
# oddcount = 0
# eventcount = 0
# evennumber = []
# for i in numbers:
#     if i % 2 == 0:
#         evennumber.append(i)
#         eventcount += 1
#     else:
#         oddnumber.append(i)
#         oddcount += 1

# print("Odd numbers:", oddnumber)
# print("Even numbers:", evennumber)
# print(f"Total odd numbers: {oddcount} and odd numbers are {oddnumber}")

# variable data validation : startwith(), endwith(), isalpha(), isdigit, islower, isupper, lower, upper -- inbuilt function 
# variables : Regular expression validation, len(), type(), split(), strip(), find() -- in built function
# function : in built function and user defined function

name = "Aritifical Intelligence"
if name.startswith("Ari"):  # pattern matching 
    print("Yes, the string starts with 'Ari'")
if name.endswith("ce"):
    print("Yes, the string ends with 'ce'")

if  "Aritifical" in name:
    print("Yes, 'Aritifical' is present in the string")
if  "Machine" not in name:
    print("No, 'Machine' is not present in the string")

email = "kumar@gmail.COM"

if email.lower().endswith(".com") and "@" in email:
    print("Valid email domain")

phone_number = "1234567890"
if phone_number.isdigit() and len(phone_number) == 10:
    print("Valid phone number")


if name.find("Intelligence"):
    print("intelligence is present in the string")

filename = " report.pdf "
if filename.strip().endswith(".pdf"):
    print("This is a PDF file")

if filename.strip().split(".")[1] == "pdf":
    print("This is a PDF file based on split method")

filename = " report.pdf "
print("This is a valid pdf" if filename.strip().endswith(".pdf") else "This is not a valid pdf")