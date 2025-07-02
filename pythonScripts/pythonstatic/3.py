class Student:
    school_name = ""  # static/class variable

# creating instance
s1 = Student()
s2 = Student()

# change using instance
s1.school_name = input("Enter school name from s1: ")  # this creates an instance variable, not change the class var

print("s1.school_name:", s1.school_name)
print("s2.school_name:", s2.school_name)
print("Student.school_name:", Student.school_name)
