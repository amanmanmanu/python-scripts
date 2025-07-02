class PrivateExample:
    def __init__(self):
        self.__name = input("Enter your name: ")
        self.__age = input("Enter your age: ")

    def __private_method(self):
        print("Private Method Called! Name:", self.__name, "Age:", self.__age)

    def access_private_method(self):
        self.__private_method()  # allowed inside class


# Main Method
print("----- Inside Main Class -----")
obj = PrivateExample()

# Accessing private fields (not directly)
# print(obj.__name)  ❌  Error

# Correct way using name mangling
print("Name (via mangling):", obj._PrivateExample__name)
print("Age (via mangling):", obj._PrivateExample__age)

# Access private method
obj._PrivateExample__private_method()


# Subclass trying to access private members
class SubPrivate(PrivateExample):
    def try_access_private(self):
        print("----- Subclass Trying to Access Private Members -----")
        try:
            print("Name:", self.__name)
        except AttributeError:
            print("Cannot access __name from subclass")

        try:
            self.__private_method()
        except AttributeError:
            print("Cannot access __private_method from subclass")


sub = SubPrivate()
sub.try_access_private()
