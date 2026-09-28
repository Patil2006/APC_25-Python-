"""
Problem Statement:
Create a Pandas Series using a dictionary where patient IDs
are the index and patient ages are the values.

Perform:
1. Find the average age.
2. Find the oldest patient.
3. Find the youngest patient.
4. Display patients above 60 years.
"""

import pandas as pd

data = {
    101: 65,
    102: 45,
    103: 72,
    104: 58,
    105: 68
}

ages = pd.Series(data)

print("Patient Ages:")
print(ages)

print("\nAverage Age:", ages.mean())
print("Oldest Patient:", ages.max())
print("Youngest Patient:", ages.min())

print("\nPatients above 60 years:")
print(ages[ages > 60])