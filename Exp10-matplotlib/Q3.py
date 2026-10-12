"""
Problem Statement:
Write a Python program to draw a pie chart showing the
percentage distribution of students in different branches.
"""

import matplotlib.pyplot as plt

branches = ["CSE", "IT", "ENTC", "Mechanical", "Civil"]
students = [40, 20, 15, 15, 10]

plt.pie(students, labels=branches, autopct="%1.1f%%")

plt.title("Percentage Distribution of Students")

plt.show()