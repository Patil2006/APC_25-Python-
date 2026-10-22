# 25. Create a dictionary containing student names and marks. Develop a program to:
# • Add a student
# • Update marks
# • Delete a student
# • Search for a student
# • Display all students
# • Find the highest marks
# • Calculate the average

students = {"Amit": 75, "Sneha": 85, "Rahul": 90}

students["Priya"] = 80

students["Amit"] = 88

del students["Rahul"]

name = "Sneha"
if name in students:
    print("Student found:", name, students[name])
else:
    print("Student not found")

print("All students:")
for name, marks in students.items():
    print(name, ":", marks)

highest = max(students.values())
print("Highest marks:", highest)

average = sum(students.values()) / len(students)
print("Average marks:", average)