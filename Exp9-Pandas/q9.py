"""
Problem Statement:
Create a Pandas Series using a dictionary containing employee
names and their salaries.

Perform:
1. Display the Series.
2. Find the highest salary.
3. Find the lowest salary.
4. Calculate average salary.
5. Display employees earning more than 50000.
"""

import pandas as pd

data = {
    "Rahul": 45000,
    "Priya": 60000,
    "Amit": 75000,
    "Sneha": 52000,
    "Rohan": 48000
}

salary = pd.Series(data)

print("Employee Salaries:")
print(salary)

print("\nHighest Salary:", salary.max())
print("Lowest Salary:", salary.min())
print("Average Salary:", salary.mean())

print("\nEmployees earning more than 50000:")
print(salary[salary > 50000])