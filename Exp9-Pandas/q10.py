"""
Problem Statement:
Create a Pandas Series using a dictionary containing product
names and prices.

Perform:
1. Display all products and prices.
2. Increase every price by 10%.
3. Find the most expensive product.
4. Find products costing more than 1000.
"""

import pandas as pd

data = {
    "Laptop": 50000,
    "Mobile": 30000,
    "Keyboard": 800,
    "Monitor": 12000,
    "Mouse": 600
}

prices = pd.Series(data)

print("Products and Prices:")
print(prices)

prices = prices * 1.10

print("\nPrices after 10% increase:")
print(prices)

print("\nMost Expensive Product:")
print(prices.idxmax(), "=", prices.max())

print("\nProducts costing more than 1000:")
print(prices[prices > 1000])