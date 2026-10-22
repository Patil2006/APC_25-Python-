"""
Problem Statement:
Create two NumPy arrays and concatenate them
horizontally and vertically.
"""

import numpy as np

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

horizontal = np.hstack((arr1, arr2))
vertical = np.vstack((arr1, arr2))

print("\nHorizontal Concatenation:")
print(horizontal)

print("\nVertical Concatenation:")
print(vertical)