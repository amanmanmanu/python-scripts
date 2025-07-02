n = int(input("Enter number of elements: "))
arr = [0] * n
for i in range(n):
    arr[i] = int(input("Enter element: "))

first = second = -999999

for i in range(n):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif arr[i] > second and arr[i] != first:
        second = arr[i]

if second == -999999:
    print("No second largest")
else:
    print("Second largest:", second)
