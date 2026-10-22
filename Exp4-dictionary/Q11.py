# Create a dictionary containing student names and marks.
# Find the student who has scored the highest marks.

students = {
    "Arpita": 85,
    "Rahul": 78,
    "Sneha": 92,
    "Amit": 80
}

highest = max(students, key=students.get)

print("Highest scorer:", highest)
print("Marks:", students[highest])