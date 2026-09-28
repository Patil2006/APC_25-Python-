# 22. Generate a random 3D array of shape (3, 4, 5)
# and calculate mean, median, standard deviation, variance,
# minimum, and maximum.

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(arr)

print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))