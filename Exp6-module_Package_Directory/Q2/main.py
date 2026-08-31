# Import the student module and generate a student's result.

import student

name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

total = student.total_marks(marks)
percent = student.percentage(marks)
grade = student.grade(percent)

print("\nStudent Result")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percent)
print("Grade:", grade)