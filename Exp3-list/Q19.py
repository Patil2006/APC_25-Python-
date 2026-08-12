"""19.	Store names of students present in class.
Display:
•	Total students 
•	Search a student's attendance 
•	Add a new student 
•	Remove an absent student 
"""

students = ["Arpita", "Rahul", "Sneha", "Amit"]

print("Total students =", len(students))

name = input("Search student: ")
if name in students:
    print("Student is present")
else:
    print("Student is absent")

new = input("Enter new student: ")
students.append(new)

absent = input("Enter absent student to remove: ")
if absent in students:
    students.remove(absent)

print("Updated student list =", students)