# 18. Create a 3D NumPy array of shape (2, 3, 4)
# containing numbers from 1 to 24 and display its dimensions, shape, and size.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nNumber of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)