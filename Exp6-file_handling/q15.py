# Q15. Remove single-line comments from a Python source file

file = open("program.py", "w")

file.write("print('Hello')\n")
file.write("# This is a comment\n")
file.write("x = 10\n")
file.write("# Another comment\n")
file.write("print(x)\n")

file.close()

file = open("program.py", "r")
output = open("without_comments.py", "w")

for line in file:
    if not line.strip().startswith("#"):
        output.write(line)

file.close()
output.close()

print("Comments removed successfully.")

file = open("without_comments.py", "r")
print(file.read())
file.close()