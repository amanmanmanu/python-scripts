arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))

key = int(input("Enter value to search: "))

found = False
for i in arr:
    if i == key:
        found = True
        break

if found:
    print("Value found")
else:
    print("Value not found")
