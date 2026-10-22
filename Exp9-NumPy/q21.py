# 21. Create a 3D array of random integers between 1 and 100.
# Replace all values greater than 50 with 0.

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Original 3D Array:")
print(arr)

arr[arr > 50] = 0

print("\nArray after replacing values greater than 50 with 0:")
print(arr)