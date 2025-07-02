class Student:
    school_name = ""  # static/class variable

# change using class
Student.school_name = input("Enter school name via class: ")

# access using multiple ways
s1 = Student()
s2 = Student()

print("s1.school_name:", s1.school_name)
print("s2.school_name:", s2.school_name)
print("Student.school_name:", Student.school_name)
