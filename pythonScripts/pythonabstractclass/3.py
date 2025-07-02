# Step 3: Base class must be defined above this
class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

    def display_details(self):
        print("This is an abstract method. Should be overridden.")

    def greet(self):
        print("Hello", self.name, "! You are", self.age, "years old.")


# Child class overriding abstract method
print("\n--- Step 3: Call Abstract Method from Child ---")
class Student2(Person):
    def __init__(self):
        super().__init__()
        self.course = input("Enter course in Student2: ")

    def display_details(self):
        print("\n--- Calling Abstract Method in Student2 ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Create instance and call the abstract method from child
obj3 = Student2()
obj3.display_details()
