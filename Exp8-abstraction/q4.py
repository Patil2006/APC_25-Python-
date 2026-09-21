# Q4. Create an abstract class FoodOrder with abstract methods calculate_bill() and delivery_charge(). Derive RestaurantOrder and HomeDeliveryOrder and implement the methods appropriately.

from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price + self.delivery_charge()

    def delivery_charge(self):
        return 50

restaurant = RestaurantOrder(500)
delivery = HomeDeliveryOrder(500)

print("Restaurant Order Bill:", restaurant.calculate_bill())
print("Restaurant Delivery Charge:", restaurant.delivery_charge())

print("Home Delivery Order Bill:", delivery.calculate_bill())
print("Home Delivery Charge:", delivery.delivery_charge())