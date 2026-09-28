"""
Problem Statement:
Create an array of 10 integers.
Replace all elements greater than 50 with 0
using NumPy Boolean indexing.
"""

import numpy as np

arr = np.array([10, 25, 55, 40, 70, 35, 90, 45, 60, 20])

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("\nArray after replacing values greater than 50:")
print(arr)