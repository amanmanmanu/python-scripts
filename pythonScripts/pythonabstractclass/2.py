# Step 1: Define the abstract-like base class first
class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

    def display_details(self):
        print("This is an abstract method. Should be overridden.")

    def greet(self):
        print("Hello", self.name, "! You are", self.age, "years old.")


# Step 2: Create subclass and access non-abstract method
print("\n--- Step 2 ---")
class Student(Person):
    def __init__(self):
        super().__init__()
        self.course = input("Enter your course: ")

    def display_details(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student_obj = Student()
student_obj.greet()

