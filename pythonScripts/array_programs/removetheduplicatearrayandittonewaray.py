n = int(input("Enter number of elements: "))
arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

new_arr = [0] * n
k = 0  

for i in range(n):
    duplicate = False
    for j in range(i):
        if arr[i] == arr[j]:
            duplicate = True
            break
    if not duplicate:
        new_arr[k] = arr[i]
        k += 1

print("Array after removing duplicates:")
for i in range(k):
    print(new_arr[i], end=" ")
