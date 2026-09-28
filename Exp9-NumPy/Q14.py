"""
Problem Statement:
Create an array containing duplicate values.
Find and display only the unique elements.
"""

import numpy as np

arr = np.array([10, 20, 30, 20, 40, 10, 50, 30, 60, 40])

print("Original Array:")
print(arr)

unique = np.unique(arr)

print("\nUnique Elements:")
print(unique)