n = int(input("Enter number of elements: "))
arr = [0] * (n + 1)

for i in range(n):
    arr[i] = int(input("Enter element: "))

pos = int(input("Enter position (0-based index): "))
val = int(input("Enter value to insert: "))

for i in range(n, pos, -1):
    arr[i] = arr[i - 1]

arr[pos] = val

print("Updated array:")
for i in range(n + 1):
    print(arr[i], end=" ")
