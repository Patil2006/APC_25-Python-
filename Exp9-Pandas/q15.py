# 15. Read the patients.csv file and perform the following operations

import pandas as pd

df = pd.read_csv("patients.csv")

print("Patient Data:")
print(df)

# 1. Display patients above 60 years
print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

# 2. Calculate average medical expense
print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

# 3. Find the patient with highest medical expense
print("\nPatient with Highest Medical Expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

# 4. Count patients for each disease
print("\nNumber of Patients for Each Disease:")
print(df["Disease"].value_counts())

# 5. Display patients whose medical expense exceeds ₹50,000
print("\nPatients with Medical Expense above ₹50,000:")
print(df[df["Medical_Expense"] > 50000])