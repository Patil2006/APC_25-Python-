# Q22. Combine the contents of two text files into a third file

file1 = open("file1.txt", "w")
file1.write("This is the content of File 1.")
file1.close()

file2 = open("file2.txt", "w")
file2.write("This is the content of File 2.")
file2.close()

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
file3 = open("combined.txt", "w")

file3.write(file1.read())
file3.write("\n")
file3.write(file2.read())

file1.close()
file2.close()
file3.close()

print("Contents combined successfully.")

file3 = open("combined.txt", "r")
print(file3.read())
file3.close()