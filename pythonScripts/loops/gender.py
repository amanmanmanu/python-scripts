gender = input("Enter gender (M/F): ").upper()

match gender:
    case "M":
        print("Male")
    case "F":
        print("Female")
    case _:
        print("Invalid input")
