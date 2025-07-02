arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))

key = int(input("Enter value to find: "))

found = False
for i in range(n):
    if arr[i] == key:
        print("Index:", i)
        found = True
        break

if not found:
    print("Value not found")
