# Step 1: Define the base class first
class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

    def display_details(self):
        print("This is an abstract method. Should be overridden.")

    def greet(self):
        print("Hello", self.name, "! You are", self.age, "years old.")


# Step 3: Child class calling abstract method
print("\n--- Step 3: Calling Abstract Method from Child ---")
class Student2(Person):
    def __init__(self):
        super().__init__()
        self.course = input("Enter course in Student2: ")

    def display_details(self):
        print("\n--- Inside Student2 ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Creating object and calling abstract method
s2 = Student2()
s2.display_details()


# Step 4: Child class calling non-abstract method
print("\n--- Step 4: Calling Non-Abstract Method from Child ---")
class Student3(Person):
    def __init__(self):
        super().__init__()
        self.course = input("Enter course in Student3: ")

    def display_details(self):
        print("\nOverridden method in Student3")

# Creating object and calling non-abstract method (greet)
s3 = Student3()
s3.greet()

