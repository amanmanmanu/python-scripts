str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

equal = True
i = 0

# Get lengths
len1 = 0
len2 = 0
for _ in str1:
    len1 += 1
for _ in str2:
    len2 += 1

if len1 != len2:
    equal = False
else:
    while i < len1:
        if str1[i] != str2[i]:
            equal = False
            break
        i += 1

if equal:
    print("Strings are equal")
else:
    print("Strings are not equal")
