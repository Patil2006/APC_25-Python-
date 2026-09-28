"""
Problem Statement:
Create a Pandas Series using a dictionary where student names
are keys and their marks are values.

Perform:
1. Display the Series.
2. Display marks of a particular student.
3. Find maximum and minimum marks.
4. Calculate the average marks.
5. Display students who scored more than 75.
"""

import pandas as pd

data = {
    "Arpita": 85,
    "Riya": 72,
    "Sneha": 90,
    "Pooja": 68,
    "Neha": 80
}

marks = pd.Series(data)

print("Student Marks:")
print(marks)

print("\nMarks of Arpita:")
print(marks["Arpita"])

print("\nMaximum Marks:", marks.max())
print("Minimum Marks:", marks.min())

print("\nAverage Marks:", marks.mean())

print("\nStudents who scored more than 75:")
print(marks[marks > 75])