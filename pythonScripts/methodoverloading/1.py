class SameTypeOverload:
    def show(self, *args):
        if len(args) == 1:
            print("You entered one number:", args[0])
        elif len(args) == 2:
            print("You entered two numbers:", args[0], "and", args[1])
        else:
            print("Unsupported number of arguments.")

# Main
obj = SameTypeOverload()
count = int(input("Enter how many integers (1 or 2): "))
if count == 1:
    n = int(input("Enter number: "))
    obj.show(n)
elif count == 2:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    obj.show(n1, n2)
else:
    print("Only 1 or 2 allowed.")
