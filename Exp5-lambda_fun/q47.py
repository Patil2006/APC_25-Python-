# Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.

students = [
    ("Arpita", 85),
    ("Rahul", 70),
    ("Sneha", 90),
    ("Amit", 65)
]

sorted_students = sorted(students, key=lambda x: x[1])

print("Students sorted according to marks:")
print(sorted_students)