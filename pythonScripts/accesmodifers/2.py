# Same file (same package)

class ProtectedExample:
    def __init__(self):
        self._email = input("Enter your email: ")

    def _protected_method(self):
        print("Protected method called! Email:", self._email)


# Any class in same package
class SamePackage:
    def access_protected(self):
        obj = ProtectedExample()
        print("Accessing protected field in same package:", obj._email)
        obj._protected_method()


# Child class in different "package"
class DifferentPackageChild(ProtectedExample):
    def access_protected_child(self):
        print("Accessing protected field from child class (diff package):", self._email)
        self._protected_method()


# Non-subclass in different "package"
class DifferentPackageNonChild:
    def access_protected(self):
        obj = ProtectedExample()
        print("Accessing protected field from non-subclass (diff package):", obj._email)
        obj._protected_method()


print("\n--- Protected Access: Same Package ---")
same = SamePackage()
same.access_protected()

print("\n--- Protected Access: Child Class (Different Package) ---")
child = DifferentPackageChild()
child.access_protected_child()

print("\n--- Protected Access: Non-Child Class (Different Package) ---")
non_child = DifferentPackageNonChild()
non_child.access_protected()
