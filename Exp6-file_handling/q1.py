# Q1. Create a file named student.txt and write student details

file = open("student.txt", "w")

file.write("Name: Bhakti\n")
file.write("Roll No: 18\n")
file.write("Branch: Computer Science and engineering\n")
file.write("Semester: 5\n")

file.close()

print("Student details written successfully.")