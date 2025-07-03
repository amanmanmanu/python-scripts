# 1. Class with default, one-argument, and two-argument constructors
class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print("One-Argument Constructor Called:", a)
        else:
            print("Two-Argument Constructor Called:", a, b)

# 2. Superclass with constructors, Child class calling them
class SuperClass:
    def __init__(self):
        print("SuperClass Default Constructor")

    def __init__(self, msg="Default from SuperClass"):
        print("SuperClass Constructor:", msg)

class ChildClass(SuperClass):
    def __init__(self):
        super().__init__("Called from ChildClass")  # Call SuperClass constructor
        print("ChildClass Constructor")

# 3. Constructor with different access levels (Python style)
class AccessModifiersDemo:
    def __init__(self):          # Public (default)
        print("Public Constructor")

    def _protected_constructor(self):  # Protected (convention)
        print("Protected Constructor")

    def __private_constructor(self):   # Private (name mangling)
        print("Private Constructor")

# 4. Constructor Attributes Example
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("Student created with attributes")

    def show(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)

# ===== Main Program =====

print("\n--- 1. Calling Multiple Constructors (Overloading) ---")
obj1 = MyClass()
obj2 = MyClass("Aman")
obj3 = MyClass("Aman", 101)

print("\n--- 2. Calling Superclass Constructor from Child ---")
child = ChildClass()

print("\n--- 3. Access Modifier Simulation in Python ---")
access_obj = AccessModifiersDemo()
access_obj._protected_constructor()   # Can still be accessed (not strictly enforced)
# access_obj.__private_constructor() # This will raise AttributeError (uncomment to test)

print("\n--- 4. Constructor Attributes Demo ---")
student1 = Student("Aman", 101)
student1.show()


