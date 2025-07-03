class DifferentTypeOverload:
    def display(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            print("You entered a string:", args[0])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], float):
            print("You entered int and float:", args[0], "and", args[1])
        else:
            print("Invalid input types.")

# Main
obj = DifferentTypeOverload()
choice = input("Enter 's' for string or 'if' for int & float: ")

if choice == 's':
    s = input("Enter a string: ")
    obj.display(s)
elif choice == 'if':
    i = int(input("Enter an integer: "))
    f = float(input("Enter a float: "))
    obj.display(i, f)
else:
    print("Invalid choice.")
s