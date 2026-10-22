# 20. Create a (2, 3, 4) array and calculate:
# Sum of all elements
# Sum of each layer
# Sum along rows
# Sum along columns

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nSum of all elements:")
print(np.sum(arr))

print("\nSum of each layer:")
print(np.sum(arr, axis=(1, 2)))

print("\nSum along rows:")
print(np.sum(arr, axis=1))

print("\nSum along columns:")
print(np.sum(arr, axis=2))