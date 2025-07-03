# 6. Custom exception class and raise from main block

class MyCustomError(Exception):
    pass

age = int(input("Enter your age: "))
if age < 18:
    raise MyCustomError("Access Denied: Age must be 18+")
else:
    print("Access granted.")
