# Define ClassOne
class ClassOne:
    def __init__(self):
        print("ClassOne Constructor Called")

    def method_one(self):
        print("Method of ClassOne Called")

# Define ClassTwo
class ClassTwo:
    def __init__(self):
        print("ClassTwo Constructor Called")

    def method_two(self):
        print("Method of ClassTwo Called")

# Main program
if __name__ == "__main__":
    # Create object of ClassOne and call its method
    obj1 = ClassOne()
    obj1.method_one()

    # Create object of ClassTwo and call its method
    obj2 = ClassTwo()
    obj2.method_two()
