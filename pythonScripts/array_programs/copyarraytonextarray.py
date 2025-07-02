n = int(input("Enter number of elements: "))
arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

copy = [0] * n
for i in range(n):
    copy[i] = arr[i]

print("Copied array:", copy)
