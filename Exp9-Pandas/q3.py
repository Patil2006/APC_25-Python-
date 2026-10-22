"""
Problem Statement:
Create a dictionary containing Product ID, Product Name,
Category, Price and Quantity.

Convert it into a Pandas DataFrame.

Calculate:
Total Amount = Price × Quantity

Then find the product having the highest total sales.
"""

import pandas as pd

data = {
    "Product ID": [101, 102, 103, 104, 105],
    "Product Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 30000, 1500, 12000, 800],
    "Quantity": [2, 5, 10, 4, 15]
}

df = pd.DataFrame(data)

print("Product DataFrame:")
print(df)

df["Total Amount"] = df["Price"] * df["Quantity"]

print("\nDataFrame with Total Amount:")
print(df)

highest_sales = df["Total Amount"].max()

print("\nProduct with Highest Total Sales:")
print(df[df["Total Amount"] == highest_sales])