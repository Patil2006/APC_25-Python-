"""
Problem Statement:
Write a Python program to draw a line graph
showing the relationship between days and temperature.
"""

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temperature = [25, 27, 26, 29, 30, 28, 32]

plt.plot(days, temperature, marker='o')

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Days vs Temperature")

plt.show()
