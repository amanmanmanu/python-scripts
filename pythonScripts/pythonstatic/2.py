class Student:
    school_name = ""  # static/class variable

#  input
Student.school_name = input("Enter school name: ")

#  instance
s1 = Student()

# access using instance
print("School name (via instance):", s1.school_name)
