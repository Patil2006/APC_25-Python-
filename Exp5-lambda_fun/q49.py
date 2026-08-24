# Take a list containing student names and marks, use functions and lambda expressions to:
# a) Calculate average marks.
# b) Filter students scoring above 75.

def process_students(students):
    marks = list(map(lambda s: s[1], students))
    average = sum(marks) / len(marks)

    above_75 = list(filter(lambda s: s[1] > 75, students))

    print("Average marks:", average)
    print("Students scoring above 75:", above_75)


students = [
    ("Arpita", 85),
    ("Rahul", 70),
    ("Sneha", 90),
    ("Amit", 65)
]

process_students(students)