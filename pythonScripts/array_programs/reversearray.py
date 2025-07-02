n = int(input("Enter number of elements: "))
arr = [0] * n
rev = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

for i in range(n):
    rev[i] = arr[n - 1 - i]

print("Reversed array:")
for i in range(n):
    print(rev[i], end=" ")
