# Q16. Create another file containing the same text in uppercase

file = open("student.txt", "r")

text = file.read()

file.close()

output = open("uppercase.txt", "w")

output.write(text.upper())

output.close()

print("Uppercase file created successfully.")