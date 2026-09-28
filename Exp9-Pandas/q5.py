"""
Problem Statement:
Create a dictionary containing Order_ID, Customer, Product,
Quantity, Price and Discount.

Create a DataFrame and calculate:
Final Amount = Quantity × Price − Discount

Then display:
1. All orders
2. Orders above 5000
3. Highest-value order
4. Average order value
"""

import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [1, 2, 3, 2, 1],
    "Price": [55000, 30000, 18000, 12000, 25000],
    "Discount": [5000, 3000, 2000, 1000, 2500]
}

df = pd.DataFrame(data)

df["Final Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final Amount"] > 5000])

highest_order = df["Final Amount"].max()

print("\nHighest-Value Order:")
print(df[df["Final Amount"] == highest_order])

average_order = df["Final Amount"].mean()

print("\nAverage Order Value:", average_order)