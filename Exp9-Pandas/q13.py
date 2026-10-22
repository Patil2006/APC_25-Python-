# 14. Read the employees.csv file and perform the following operations

import pandas as pd

df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

# 1. Display employees from the CSE department
print("\nEmployees from CSE Department:")
print(df[df["Department"] == "CSE"])

# 2. Find the average salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# 3. Find the highest and lowest salary
print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

# 4. Display employees having salary greater than ₹50,000
print("\nEmployees with Salary greater than ₹50,000:")
print(df[df["Salary"] > 50000])

# 5. Calculate department-wise average salary
print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())