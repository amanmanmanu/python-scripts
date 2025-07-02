class A:
    def __init__(self):
        self.value = "A class value"

class B(A):
    def __init__(self):
        super().__init__()
        self.value = "B class value"

class C(B):
    def __init__(self):
        super().__init__()
        self.value = "C class value"

# Main execution
print("\n--- Data Member Polymorphism ---")
a = A()
b = B()
c = C()

print("A class value via A object:", a.value)
print("B class value via B object:", b.value)
print("C class value via C object:", c.value)

ref = b  # Superclass reference to B
print("Access via superclass reference to B object:", ref.value)

ref = c  # Superclass reference to C
print("Access via superclass reference to C object:", ref.value)
