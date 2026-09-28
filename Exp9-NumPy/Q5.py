"""
Problem Statement:
Create a one-dimensional array containing numbers from 1 to 12.
Reshape it into 2 × 6, 3 × 4, and 4 × 3 matrices.
"""

import numpy as np

arr = np.arange(1, 13)

print("Original Array:")
print(arr)

print("\n2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("\n3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("\n4 x 3 Matrix:")
print(arr.reshape(4, 3))        