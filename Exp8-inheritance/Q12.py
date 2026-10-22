"""
Problem Statement:
Create a class Product with product ID, name, and price.
Derive ElectronicProduct with additional attributes such as brand
and warranty. Calculate the final price after applying a discount.
"""

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        discount = self.price * 10 / 100
        final_price = self.price - discount

        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")
        print("Final Price:", final_price)


p = ElectronicProduct(101, "Laptop", 50000, "Dell", 2)

p.display()