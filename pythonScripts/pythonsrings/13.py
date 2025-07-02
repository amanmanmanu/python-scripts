text = input("Enter a string: ")

upper = ""
lower = ""

for ch in text:
    ascii_val = ord(ch)

    # To uppercase
    if ascii_val >= 97 and ascii_val <= 122:
        upper += chr(ascii_val - 32)
    else:
        upper += ch

    # To lowercase
    if ascii_val >= 65 and ascii_val <= 90:
        lower += chr(ascii_val + 32)
    else:
        lower += ch

print("Uppercase:", upper)
print("Lowercase:", lower)
