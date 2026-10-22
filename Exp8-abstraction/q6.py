# Q6. Create an abstract class Transport with an abstract method calculate_fare(distance). Implement subclasses Bus, Train, Taxi, and Flight. Calculate the fare according to the transportation type.

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2

class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5

class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10

class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 8

bus = Bus()
train = Train()
taxi = Taxi()
flight = Flight()

distance = 100

print("Bus Fare:", bus.calculate_fare(distance))
print("Train Fare:", train.calculate_fare(distance))
print("Taxi Fare:", taxi.calculate_fare(distance))
print("Flight Fare:", flight.calculate_fare(distance))