# 23. Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return total / 5

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def class_average(students):
    total = 0
    for student in students:
        total += student["percentage"]
    return total / len(students)

def highest_scorer(students):
    highest = students[0]
    for student in students:
        if student["percentage"] > highest["percentage"]:
            highest = student
    return highest

def lowest_scorer(students):
    lowest = students[0]
    for student in students:
        if student["percentage"] < lowest["percentage"]:
            lowest = student
    return lowest

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = []

    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

for student in students:
    print("\nName =", student["name"])
    print("Roll Number =", student["roll"])
    print("Total =", student["total"])
    print("Percentage =", student["percentage"])
    print("Grade =", student["grade"])

print("\nClass Average =", class_average(students))

highest = highest_scorer(students)
print("Highest Scorer =", highest["name"])
print("Highest Percentage =", highest["percentage"])

lowest = lowest_scorer(students)
print("Lowest Scorer =", lowest["name"])
print("Lowest Percentage =", lowest["percentage"])