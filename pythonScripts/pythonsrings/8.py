text = input("Enter a string: ")
prefix = input("Enter prefix: ")
suffix = input("Enter suffix: ")

# Get lengths
t_len = 0
p_len = 0
s_len = 0
for _ in text:
    t_len += 1
for _ in prefix:
    p_len += 1
for _ in suffix:
    s_len += 1

# startsWith
starts = True
if p_len > t_len:
    starts = False
else:
    for i in range(p_len):
        if text[i] != prefix[i]:
            starts = False
            break

# endsWith
ends = True
if s_len > t_len:
    ends = False
else:
    for i in range(s_len):
        if text[t_len - s_len + i] != suffix[i]:
            ends = False
            break

print("Starts with prefix?", starts)
print("Ends with suffix?", ends)

# compareTo
str1 = input("Enter first string to compare: ")
str2 = input("Enter second string to compare: ")

l1 = 0
l2 = 0
for _ in str1:
    l1 += 1
for _ in str2:
    l2 += 1

min_len = l1 if l1 < l2 else l2
result = 0

for i in range(min_len):
    if str1[i] != str2[i]:
        result = ord(str1[i]) - ord(str2[i])
        break

if result == 0:
    result = l1 - l2

if result < 0:
    print("First string is smaller")
elif result > 0:
    print("First string is greater")
else:
    print("Strings are equal")
