"""
Problem Statement:
Create a NumPy array containing numbers from 1 to 20.
Using slicing, display the first 5 elements, last 5 elements,
alternate elements, and elements in reverse order.
"""

import numpy as np

arr = np.arange(1, 21)

print("Array:")
print(arr)

print("\nFirst 5 Elements:")
print(arr[:5])

print("\nLast 5 Elements:")
print(arr[-5:])

print("\nAlternate Elements:")
print(arr[::2])

print("\nReverse Order:")
print(arr[::-1])