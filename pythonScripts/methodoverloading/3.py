class SameSignature:
    def calculate(self, a, b):
        print("Sum:", a + b)
        print("Difference:", a - b)
        print("Product:", a * b)

# Main
obj = SameSignature()
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
obj.calculate(x, y)
