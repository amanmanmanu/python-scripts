n = int(input("Enter number of elements: "))
arr = [0] * n
for i in range(n):
    arr[i] = int(input("Enter element: "))

min_val = arr[0]
max_val = arr[0]

for i in range(1, n):
    if arr[i] < min_val:
        min_val = arr[i]
    if arr[i] > max_val:
        max_val = arr[i]

print("Minimum:", min_val)
print("Maximum:", max_val)
