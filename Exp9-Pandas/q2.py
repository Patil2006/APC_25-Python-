"""
Problem Statement:
Create a dictionary containing Employee ID, Employee Name,
Department, Salary and Experience.

Convert it into a Pandas DataFrame and:
1. Display employees with salary greater than 50000.
2. Find the average salary.
3. Find the highest salary.
4. Find the employee with the highest experience.
"""

import pandas as pd

data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales"],
    "Salary": [45000, 60000, 75000, 52000, 48000],
    "Experience": [2, 5, 8, 4, 6]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)

print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

highest_salary = df["Salary"].max()
print("Highest Salary:", highest_salary)

highest_experience = df["Experience"].max()
print("\nEmployee with Highest Experience:")
print(df[df["Experience"] == highest_experience])