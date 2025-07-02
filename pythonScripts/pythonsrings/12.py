num = int(input("Enter an integer: "))

# Handle zero
if num == 0:
    print("String is: 0")
else:
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    str_num = ""
    while num > 0:
        digit = num % 10
        str_num = chr(digit + 48) + str_num
        num = num // 10

    if is_negative:
        str_num = '-' + str_num

    print("Integer as string:", str_num)
