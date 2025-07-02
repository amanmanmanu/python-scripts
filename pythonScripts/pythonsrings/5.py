text = input("Enter a string: ")
char = input("Enter character to search: ")
position = -1
index = 0
for ch in text:
    if ch == char:
        position = index
        break
    index += 1

if position == -1:
    print("Character not found")
else:
    print("Index of character:", position)
