"""
Problem Statement:
Create a class Product with product name and price.
Overload the == and > operators to compare two products based on their prices.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 50000)
p3 = Product("Tablet", 30000)

if p1 == p2:
    print("Laptop and Mobile have same price")

if p1 > p3:
    print("Laptop is more expensive than Tablet")