text = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
result = ""
index = 0
for ch in text:
    if index >= start and index < end:
        result += ch
    index += 1
print("Substring is:", result)
