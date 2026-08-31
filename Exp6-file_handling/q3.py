# Q3. Append additional student information without deleting previous contents
file = open("student.txt", "a")
file.write("College: DYP\n")
file.write("City: Kolhapur\n")
file.close()
print("Information append successfully")