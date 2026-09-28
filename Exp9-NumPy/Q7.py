"""
Problem Statement:
Create two compatible matrices using NumPy and perform
matrix multiplication using an appropriate NumPy function.
"""

import numpy as np

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Multiplication:")
print(result)