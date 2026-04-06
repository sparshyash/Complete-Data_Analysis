import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "geek.txt")

f = open(file_path, "r")
content = f.read()
print(content)
f.close()

f = open(file_path, "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

with open(file_path, "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

# When using with, the file closes automatically at the end of the block.


try:
    file = open("geeks.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
    print("File Closed")
# It's important to handle exceptions to ensure that files are closed properly, even if an error occurs during file operations. Here, the finally block ensures the file is closed even if an error occurs.


lines = ["First line\n", "Second line\n", "Third line\n"]

with open(file_path, "w") as f:
    f.writelines(lines)
