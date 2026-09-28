"""
Problem Statement:
A retail shop maintains sales information in a Python dictionary
containing Product_ID, Product_Name, Category, Price, and Quantity.

Write a Python program to:
1. Convert the dictionary into a Pandas DataFrame.
2. Add a new column Total_Sales.
3. Calculate total sales using Price × Quantity.
4. Display products with sales greater than 10000.
5. Find the product with maximum sales.
6. Calculate the average sales.
"""

import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 30000, 1500, 12000, 25000],
    "Quantity": [2, 5, 10, 4, 1]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Product DataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

max_sales = df["Total_Sales"].max()

print("\nProduct with Maximum Sales:")
print(df[df["Total_Sales"] == max_sales])

average_sales = df["Total_Sales"].mean()

print("\nAverage Sales:", average_sales)