text = input("Enter a sentence: ")

words = []
current = ""
for ch in text:
    if ch != ' ':
        current += ch
    else:
        if current != "":
            words.append(current)
            current = ""
if current != "":
    words.append(current)

print("Words:")
for word in words:
    print(word)
