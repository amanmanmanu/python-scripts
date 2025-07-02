arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))

key = int(input("Enter value to remove: "))

if key in arr:
    arr.remove(key)
    print("Updated array:", arr)
else:
    print("Value not found")
