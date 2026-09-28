"""
Problem Statement:
Create a dictionary containing Student_ID, Name, Department,
Total_Classes and Classes_Attended.

Create a DataFrame and calculate:
Attendance Percentage = (Classes_Attended / Total_Classes) × 100

Display students whose attendance is below 75%.
"""

import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Arpita", "Riya", "Sneha", "Pooja", "Neha"],
    "Department": ["CSE", "CSE", "IT", "CSE", "IT"],
    "Total_Classes": [50, 50, 60, 40, 50],
    "Classes_Attended": [45, 35, 50, 25, 42]
}

df = pd.DataFrame(data)

df["Attendance Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("Student Attendance DataFrame:")
print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance Percentage"] < 75])