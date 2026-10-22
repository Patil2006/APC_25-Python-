# Import functions from student package.

from student.marks import total_marks, percentage
from student.grade import calculate_grade
from student.attendance import attendance_eligibility

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

attendance = float(input("Enter attendance percentage: "))

total = total_marks(marks)
percent = percentage(marks)
grade = calculate_grade(percent)
eligibility = attendance_eligibility(attendance)

print("\n----- Student Report -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percent)
print("Grade:", grade)
print("Attendance:", attendance, "%")
print("Eligibility:", eligibility)