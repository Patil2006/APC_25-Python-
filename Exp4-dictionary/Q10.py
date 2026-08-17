# Accept five student names and their marks from the user and store them in a dictionary.

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print(students)