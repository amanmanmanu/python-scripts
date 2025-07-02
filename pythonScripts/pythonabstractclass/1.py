class Person:
    def __init__(self):
        self.name = input("Enter your name: ")  # Fixed: Proper indentation
        self.age = input("Enter your age: ")    # Fixed: Proper indentation
    
    def display_details(self):
        print("This is an abstract method. Should be overridden.")  # Fixed: Proper indentation
    
    def greet(self):
        print("Hello", self.name, "! You are", self.age, "years old.")
        return

# Create an instance of Person to trigger input
person = Person()
person.greet()  # Call greet() to see output
