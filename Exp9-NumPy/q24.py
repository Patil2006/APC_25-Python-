# 24. Create a 3D array containing integers from 1 to 27.
# Flatten the array and calculate sum, average, maximum, and minimum.

import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)

print("3D Array:")
print(arr)

flat = arr.flatten()

print("\nFlattened Array:")
print(flat)

print("\nSum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))