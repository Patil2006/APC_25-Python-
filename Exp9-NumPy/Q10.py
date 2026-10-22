"""
Problem Statement:
Create a 4 × 4 matrix and calculate the sum of each row
and each column separately.
"""

import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:")
print(matrix)

row_sum = np.sum(matrix, axis=1)
column_sum = np.sum(matrix, axis=0)

print("\nSum of Each Row:")
print(row_sum)

print("\nSum of Each Column:")
print(column_sum)