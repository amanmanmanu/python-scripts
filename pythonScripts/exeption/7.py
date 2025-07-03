# 7. finally block execution

num = int(input("Enter a number to divide 50 by: "))
try:
    result = 50 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Caught division by zero")
finally:
    print("This is the finally block. It always runs.")
