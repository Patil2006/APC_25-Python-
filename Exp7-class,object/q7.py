# Q7. Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

phone = MobilePhone("Samsung", "Galaxy A55", "128GB", 30000)

phone.display()
print("Price after discount:", phone.discounted_price(10))