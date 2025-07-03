# 11. IOError (simulate by trying to open a file wrongly)

filename = input("Enter filename to read (try missing.txt): ")

try:
    with open(filename, "r") as file:
        print(file.read())
except IOError as e:
    print("Caught IOError:", e)
