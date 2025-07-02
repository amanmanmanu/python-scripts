
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print("Smaller number:", a)
    print("Larger number:", b)
elif a > b:
    print("Smaller number:", b)
    print("Larger number:", a)
else:
    print("Both numbers are equal.")
