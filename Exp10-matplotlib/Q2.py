"""
Problem Statement:
Write a Python program to draw a bar chart representing
the population of different cities using Matplotlib.
"""

import matplotlib.pyplot as plt

cities = ["Mumbai", "Pune", "Delhi", "Chennai", "Kolkata"]
population = [20, 7, 32, 11, 15]

plt.bar(cities, population)

plt.title("Population of Different Cities")
plt.xlabel("Cities")
plt.ylabel("Population (in millions)")

plt.show()