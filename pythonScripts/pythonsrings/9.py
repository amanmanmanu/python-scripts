text = input("Enter a string with spaces: ")

# Get total length
length = 0
for _ in text:
    length += 1

# Find first non-space
start = 0
while start < length and (text[start] == ' ' or text[start] == '\t'):
    start += 1

# Find last non-space
end = length - 1
while end >= 0 and (text[end] == ' ' or text[end] == '\t'):
    end -= 1

# Extract trimmed string
trimmed = ""
i = start
while i <= end:
    trimmed += text[i]
    i += 1

print("Trimmed string:", trimmed)
