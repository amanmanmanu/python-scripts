# 9. FileNotFoundError

filename = input("Enter filename to open (try wrong name): ")
with open(filename, "r") as f:
    data = f.read()
    print(data)
