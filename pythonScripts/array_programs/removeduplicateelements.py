n = int(input("Enter number of elements: "))
arr = [0] * n
unique = [0] * n
k = 0

for i in range(n):
    arr[i] = int(input("Enter element: "))
    already_exists = False
    for j in range(k):
        if unique[j] == arr[i]:
            already_exists = True
            break
    if not already_exists:
        unique[k] = arr[i]
        k += 1

print("Array without duplicates:")
for i in range(k):
    print(unique[i], end=" ")
