# 1.1 Adding values to dictionary
students = {
    "S101": "Aman",
    "S102": "Rahul",
    "S103": "Priya",
    "S104": "Fatima",
    "S105": "John"
}
print("Initial Dictionary:")
print(students)

# 1.2 Updating a value in dictionary
students["S103"] = "Pooja"
print("\nAfter Updating S103:")
print(students)

# 1.3 Accessing a value
sid = input("\nEnter Student ID to access name (e.g., S102): ")
if sid in students:
    print("Student Name:", students[sid])
else:
    print("ID not found")

# 1.4 Creating a nested dictionary
nested_students = {
    "S201": {"name": "Ali", "age": 21, "grade": "A"},
    "S202": {"name": "Meena", "age": 22, "grade": "B"},
    "S203": {"name": "Raj", "age": 20, "grade": "A"},
}
print("\nNested Dictionary:")
print(nested_students)

# 1.5 Access values from nested dictionary
nested_id = input("\nEnter Nested Student ID to access details (e.g., S202): ")
if nested_id in nested_students:
    print("Student Details:")
    for key, value in nested_students[nested_id].items():
        print(f"{key}: {value}")
else:
    print("Nested ID not found")

# 1.6 Print keys in a dictionary
print("\nAll Student IDs in the original dictionary:")
print(list(students.keys()))

# 1.7 Deleting a value from dictionary
del_id = input("\nEnter Student ID to delete (e.g., S104): ")
if del_id in students:
    del students[del_id]
    print(f"Deleted {del_id}. Updated Dictionary:")
    print(students)
else:
    print("ID not found to delete.")
