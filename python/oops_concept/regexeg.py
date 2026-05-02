import re

text = input("enter text")
bpat = input("enter beginning pattern")
epat = input("enter ending pattern")
username = input("enter username: ")

if re.search(bpat, text):
    print("beginning pattern available")
else:
    print("beginning pattern not available")
if re.search(epat, text):
    print("ending pattern available")
else:
    print("beginning pattern not available")


# pattern = f"{bpat}.*{epat}"
#
# if re.fullmatch(pattern, text):
#     print("Full match: begins and ends with given patterns")
# else:
#     print("No full match")

# pattern = r"^[A-Za-z][A-Za-z0-9_]{2,14}$"
# if re.fullmatch(pattern, username):
#     print("Valid username")
# else:
#     print("Invalid username")



# email = input("Enter email: ")
#
# pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
#
# if re.fullmatch(pattern, email):
#     print("Valid email")
# else:
#     print("Invalid email")

text = "This   is   a   test"
parts = re.split(r"\s+", text)

print(parts)