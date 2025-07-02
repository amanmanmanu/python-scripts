n = int(input("Enter number of elements: "))
arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

found12 = False
found23 = False

for i in range(n):
    if arr[i] == 12:
        found12 = True
    if arr[i] == 23:
        found23 = True

if found12 and found23:
    print("Both 12 and 23 are present")
else:
    print("One or both values not found")
