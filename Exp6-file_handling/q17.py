# Q17. Student records: display, highest marks, average and students above 80

file = open("students.txt", "r")

students = []

file.readline()  # Skip heading

for line in file:
    roll, name, marks = line.strip().split(",")
    students.append((roll, name, int(marks)))

file.close()

print("All Records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print(highest)

average = sum(student[2] for student in students) / len(students)

print("\nAverage Marks:", average)

print("\nStudents scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student)