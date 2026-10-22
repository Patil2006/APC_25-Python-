"""
Problem Statement:
Write a Python program to draw a scatter plot showing
the relationship between hours studied and marks obtained.
"""

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 80, 90]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")

plt.show()