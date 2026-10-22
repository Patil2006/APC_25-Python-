"""
Problem Statement:
Create a 3 × 4 matrix and display its transpose.
"""

import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

transpose = matrix.T

print("Original Matrix:")
print(matrix)

print("\nTranspose of Matrix:")
print(transpose)