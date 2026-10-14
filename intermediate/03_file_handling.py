# ==========================================
# FILE HANDLING: Reading and writing to text files
# ==========================================

# Writing to a file (Mode 'w' creates the file or overwrites it if it already exists)
print("Writing data to a file...")
with open("notes.txt", "w") as file:
    file.write("Python File Handling Notes:\n")
    file.write("1. Always use the 'with' keyword so files close automatically.\n")
    file.write("2. 'w' writes, 'a' appends, 'r' reads.\n")

# Appending to a file (Mode 'a' adds text to the bottom without erasing old stuff)
with open("notes.txt", "a") as file:
    file.write("3. Appending keeps your old data safe!\n")

print("Reading data back from the file:\n")
# Reading from a file (Mode 'r')
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
