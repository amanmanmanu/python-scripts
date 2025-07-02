# Global variable (user-defined)
x = int(input("Enter a value for global variable x: "))

def show_scope():
    # Local variable with same name (user-defined)
    x = int(input("Enter a value for local variable x (inside function): "))
    print("Local x inside function:", x)

# Call function
show_scope()

# Print global x
print("Global x outside function:", x)
