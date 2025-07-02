class Student:
    school_name = ""  # static/class variable

#  input
Student.school_name = input("Enter school name: ")

# access using class
print("School name (via class):", Student.school_name)
