"""
Problem Statement:
Create a dictionary containing information for 5 students:
Student ID, Student Name, Python Marks, DBMS Marks,
and Mathematics Marks.

Convert the dictionary into a Pandas DataFrame and:
1. Display the DataFrame.
2. Calculate total marks for each student.
3. Calculate average marks.
4. Display students who scored more than 75% average.
"""

import pandas as pd

data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Arpita", "Riya", "Sneha", "Pooja", "Neha"],
    "Python Marks": [85, 72, 90, 65, 80],
    "DBMS Marks": [80, 75, 88, 70, 85],
    "Mathematics Marks": [90, 68, 92, 72, 78]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

df["Total Marks"] = (
    df["Python Marks"] +
    df["DBMS Marks"] +
    df["Mathematics Marks"]
)

df["Average Marks"] = df["Total Marks"] / 3

print("\nDataFrame with Total and Average Marks:")
print(df)

print("\nStudents with Average Marks greater than 75%:")
print(df[df["Average Marks"] > 75])