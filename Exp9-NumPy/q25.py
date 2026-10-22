# 25. Create a random 3D NumPy array of shape (3, 4, 5).
# Flatten it and display elements greater than 50, even numbers,
# and elements less than the average value.

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(arr)

flat = arr.flatten()

print("\nFlattened Array:")
print(flat)

print("\nElements greater than 50:")
print(flat[flat > 50])

print("\nEven numbers:")
print(flat[flat % 2 == 0])

average = np.mean(flat)

print("\nAverage:", average)

print("\nElements less than average:")
print(flat[flat < average])