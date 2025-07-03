# 12. NoSuchFieldException in Python → AttributeError

class Student:
    def __init__(self):
        self.name = "Aman"

s = Student()
print("Accessing non-existent attribute...")
print(s.age)  # No such field → AttributeError
