n = int(input("Enter number of elements: "))
arr = [0] * n
even = 0
odd = 0

for i in range(n):
    arr[i] = int(input("Enter element: "))
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
