"""
Problem Statement:
Create a base class Vehicle with a method start().
Derive Car, Bike, and Bus classes and override start()
to display the starting behavior of each vehicle.
"""

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")


vehicles = [
    Car(),
    Bike(),
    Bus()
]

for vehicle in vehicles:
    vehicle.start()