arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))

total = 0
for num in arr:
    total += num

average = total / n
print("Average:", average)
