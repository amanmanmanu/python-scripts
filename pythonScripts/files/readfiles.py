# Step 1: Create and write to sample.txt
text = input("Enter text to write to 'sample.txt': ")

with open("sample.txt", "w") as file:
    file.write(text)

print("\n✅ Text written to sample.txt")

# Step 2: Read the entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\n📄 Full File Content:\n", content)

# Step 3: Read file line by line (stream)
print("\n📄 Reading line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# Step 4: Random access using seek()
with open("sample.txt", "r") as file:
    file.seek(5)  # start from 5th byte
    random_read = file.read(15)
    print("\n🔁 Random Access (from byte 5, next 15 chars):", random_read)

# Step 5: Seek to user-given index and read from there
index = int(input("\nEnter byte index to seek and read: "))
with open("sample.txt", "r") as file:
    file.seek(index)
    print("📍 Reading from index", index, ":", file.readline())

# Step 6: Check file read/write permissions
import os

filename = "sample.txt"
print("\n🔒 File Access Check for:", filename)

if os.access(filename, os.R_OK):
    print("✅ File is readable")
else:
    print("❌ File is NOT readable")

if os.access(filename, os.W_OK):
    print("✅ File is writable")
else:
    print("❌ File is NOT writable")
