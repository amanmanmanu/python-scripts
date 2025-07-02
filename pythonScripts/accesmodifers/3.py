class PublicExample:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.city = input("Enter your city: ")

    def display(self):
        print("Name:", self.name, "| City:", self.city)


# Any class (same or different file)
class AnyOtherClass:
    def access_public(self):
        obj = PublicExample()
        print("Accessing public fields:", obj.name, obj.city)
        obj.display()


print("\n--- Public Access ---")
public_obj = PublicExample()
public_obj.display()

print("\n--- Public Access from Another Class ---")
other = AnyOtherClass()
other.access_public()
