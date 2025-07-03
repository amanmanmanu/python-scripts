# 4. Multiple except blocks

try:
    arr = [10, 20, 30]
    index = int(input("Enter index to access (0 to 2): "))
    print("Value:", arr[index])

    num = int(input("Enter number to divide 100 by: "))
    print("Result:", 100 / num)

except IndexError:
    print("Error: Index out of range")
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("Other Exception:", e)
