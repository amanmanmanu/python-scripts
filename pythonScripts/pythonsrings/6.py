text = input("Enter a string (only letters allowed): ")
is_valid = True

for ch in text:
    ascii_val = ord(ch)
    if not ((ascii_val >= 65 and ascii_val <= 90) or (ascii_val >= 97 and ascii_val <= 122)):
        is_valid = False
        break

if is_valid:
    print("Match found! Only letters")
else:
    print("Invalid: Contains non-letter characters")
