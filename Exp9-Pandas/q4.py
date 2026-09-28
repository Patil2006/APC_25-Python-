"""
Problem Statement:
Create a dictionary containing Patient ID, Patient Name, Age,
Disease and Medical Charges.

Convert the dictionary into a Pandas DataFrame and:
1. Display patients above 60 years.
2. Find the average medical charge.
3. Find the maximum medical charge.
4. Display patients whose medical charges are greater than 50000.
"""

import pandas as pd

data = {
    "Patient ID": [101, 102, 103, 104, 105],
    "Patient Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Age": [65, 45, 72, 58, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical Charges": [55000, 15000, 80000, 30000, 65000]
}

df = pd.DataFrame(data)

print("Patient DataFrame:")
print(df)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

average_charge = df["Medical Charges"].mean()
print("\nAverage Medical Charge:", average_charge)

maximum_charge = df["Medical Charges"].max()
print("Maximum Medical Charge:", maximum_charge)

print("\nPatients with Medical Charges greater than 50000:")
print(df[df["Medical Charges"] > 50000])