# Q6. Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 1.5
        elif self.units <= 200:
            bill = (100 * 1.5) + ((self.units - 100) * 2.5)
        elif self.units <= 300:
            bill = (100 * 1.5) + (100 * 2.5) + ((self.units - 200) * 4)
        else:
            bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((self.units - 300) * 5)

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())

bill = ElectricityBill(1001, "Rahul", 250)
bill.display()