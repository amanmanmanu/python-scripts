# 1. Arithmetic Exception without handling

num = int(input("Enter a number to divide 10 by (try 0 to see exception): "))
result = 10 / num  # ZeroDivisionError if num == 0
print("Result:", result)

