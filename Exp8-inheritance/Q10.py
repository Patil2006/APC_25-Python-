"""
Problem Statement:
Create a base class Vehicle.
Derive Car and Bike from Vehicle.
Create a class SportsCar that inherits from Car and another class
ElectricBike that inherits from Bike.
Add suitable attributes and methods to demonstrate a combination
of inheritance types.
"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def car_details(self, model):
        self.model = model
        print("Model:", self.model)


class Bike(Vehicle):
    def bike_details(self, engine):
        self.engine = engine
        print("Engine:", self.engine)


class SportsCar(Car):
    def sports_details(self, speed):
        self.speed = speed
        print("Top Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def electric_details(self, battery):
        self.battery = battery
        print("Battery:", self.battery, "kWh")


s = SportsCar("BMW")
s.display()
s.car_details("M4")
s.sports_details(250)

print()

e = ElectricBike("Ather")
e.display()
e.bike_details("Electric")
e.electric_details(5)