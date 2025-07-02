class A:
    def __init__(self):
        self.a1 = input("Enter A class variable a1: ")
        self.a2 = input("Enter A class variable a2: ")

    def show(self):
        print("A class override method")

    def a_method1(self):
        print("A class method 1:", self.a1)

    def a_method2(self):
        print("A class method 2:", self.a2)


class B(A):
    def __init__(self):
        super().__init__()
        self.b1 = input("Enter B class variable b1: ")
        self.b2 = input("Enter B class variable b2: ")

    def show(self):
        print("B class override method")

    def b_method1(self):
        print("B class method 1:", self.b1)

    def b_method2(self):
        print("B class method 2:", self.b2)


class C(B):
    def __init__(self):
        super().__init__()
        self.c1 = input("Enter C class variable c1: ")
        self.c2 = input("Enter C class variable c2: ")

    def show(self):
        print("C class override method")

    def c_method1(self):
        print("C class method 1:", self.c1)

    def c_method2(self):
        print("C class method 2:", self.c2)


# Main Execution
print("\n--- Object of Class A ---")
objA = A()
objA.a_method1()
objA.a_method2()
objA.show()

print("\n--- Object of Class B ---")
objB = B()
objB.a_method1()
objB.a_method2()
objB.b_method1()
objB.b_method2()
objB.show()

print("\n--- Object of Class C ---")
objC = C()
objC.a_method1()
objC.a_method2()
objC.b_method1()
objC.b_method2()
objC.c_method1()
objC.c_method2()
objC.show()

# Runtime Polymorphism: superclass reference
print("\n--- Runtime Polymorphism ---")
ref: A = objB
ref.show()

ref = objC
ref.show()
