# 2. Handling Arithmetic Exception using try-except

num = int(input("Enter a number to divide 10 by: "))

try:
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
