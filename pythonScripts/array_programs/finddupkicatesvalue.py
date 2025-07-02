n = int(input("Enter number of elements: "))
arr = [0] * n
for i in range(n):
    arr[i] = int(input("Enter element: "))

print("Duplicate elements:")
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            duplicate = False
            for k in range(i):
                if arr[k] == arr[i]:
                    duplicate = True
                    break
            if not duplicate:
                print(arr[i])
