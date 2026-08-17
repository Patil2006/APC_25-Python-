# 5. Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.

students = {"Bhakti", "Aditi", "Sneha", "Priya", "Neha"}

name = input("Enter student name: ")

if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")