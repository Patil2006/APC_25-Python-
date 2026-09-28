"""
Problem Statement:
Create a Pandas Series using a dictionary containing student
names and attendance percentages.

Perform:
1. Find the average attendance.
2. Display students with attendance below 75%.
3. Display students with attendance above 90%.
4. Find the highest attendance.
"""

import pandas as pd

data = {
    "Arpita": 92,
    "Riya": 72,
    "Sneha": 95,
    "Pooja": 68,
    "Neha": 85
}

attendance = pd.Series(data)

print("Student Attendance:")
print(attendance)

print("\nAverage Attendance:", attendance.mean())

print("\nStudents with attendance below 75%:")
print(attendance[attendance < 75])

print("\nStudents with attendance above 90%:")
print(attendance[attendance > 90])

print("\nHighest Attendance:", attendance.max())