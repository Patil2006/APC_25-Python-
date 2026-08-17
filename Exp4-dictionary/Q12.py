# Create a dictionary containing student names and marks.
# Find the student with the lowest marks.

students = {
    "Arpita": 85,
    "Rahul": 78,
    "Sneha": 92,
    "Amit": 65
}

lowest = min(students, key=students.get)

print("Lowest scorer:", lowest)
print("Marks:", students[lowest])