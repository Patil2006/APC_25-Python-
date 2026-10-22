"""
Problem Statement:
Create an unsorted NumPy array and display it in
ascending order and descending order.
"""

import numpy as np

arr = np.array([45, 12, 78, 23, 56, 9, 34, 67])

print("Original Array:")
print(arr)

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("\nAscending Order:")
print(ascending)

print("\nDescending Order:")
print(descending)