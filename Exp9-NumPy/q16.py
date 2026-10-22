# 16. Store marks of 10 students in a NumPy array.
# Calculate highest marks, lowest marks, average, median, and standard deviation.

import numpy as np

marks = np.array([75, 82, 68, 91, 56, 88, 73, 95, 64, 79])

print("Marks of 10 Students:")
print(marks)

print("\nHighest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))