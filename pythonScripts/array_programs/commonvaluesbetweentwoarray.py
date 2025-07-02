n1 = int(input("Enter number of elements in first array: "))
arr1 = [0] * n1
for i in range(n1):
    arr1[i] = int(input("Enter element: "))

n2 = int(input("Enter number of elements in second array: "))
arr2 = [0] * n2
for i in range(n2):
    arr2[i] = int(input("Enter element: "))

print("Common elements:")
for i in range(n1):
    for j in range(n2):
        if arr1[i] == arr2[j]:
            duplicate = False
            for k in range(i):
                if arr1[k] == arr1[i]:
                    duplicate = True
                    break
            if not duplicate:
                print(arr1[i])
