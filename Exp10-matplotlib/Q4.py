"""
Problem Statement:
Write a Python program to draw a histogram representing
the distribution of students' marks.
"""

import matplotlib.pyplot as plt

marks = [45, 56, 67, 78, 89, 34, 55, 67, 78, 90,
         65, 72, 81, 49, 58, 76, 88, 92, 61, 70]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Students' Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()