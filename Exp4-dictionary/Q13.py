# Create a dictionary containing student names and marks.
# Calculate the average marks of all students.

students = {
    "Arpita": 85,
    "Rahul": 78,
    "Sneha": 92,
    "Amit": 80
}

average = sum(students.values()) / len(students)

print("Average marks:", average)