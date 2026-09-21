# Q10. Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully")

    def calculate_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.availability)

v = Vehicle("MH12AB1234", "Swift", 1000, True)

v.display()
v.rent_vehicle()
print("Rental Charges:", v.calculate_charges(3))
v.return_vehicle()
v.display()