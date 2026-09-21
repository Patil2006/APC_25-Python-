# Q11. Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, product, price):
        self.products[product] = price
        print(product, "added to cart")

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]
            print(product, "removed from cart")
        else:
            print(product, "not found in cart")

    def total_bill(self):
        return sum(self.products.values())

    def display(self):
        print("Customer Name:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:", self.products)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed")

cart = ShoppingCart("Rahul", "C101")

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

cart.display()

cart.remove_product("Mouse")

cart.display()

del cart