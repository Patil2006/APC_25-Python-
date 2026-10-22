# 23. Create a 3D NumPy array of shape (2, 3, 4)
# containing numbers from 1 to 24.
# Flatten the array and display both arrays.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D Array:")
print(arr)

flat = arr.flatten()

print("\nFlattened 1D Array:")
print(flat)