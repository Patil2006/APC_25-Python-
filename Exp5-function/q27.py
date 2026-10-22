# 27. Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.

def consultation_charges(amount):
    return amount

def laboratory_charges(amount):
    return amount

def medicine_charges(amount):
    return amount

def room_charges(days, rate):
    return days * rate

def calculate_discount(total, category):
    if category.lower() == "senior":
        return total * 0.20
    elif category.lower() == "student":
        return total * 0.10
    else:
        return 0

def final_bill(consultation, laboratory, medicine, room, category):
    total = consultation + laboratory + medicine + room
    discount = calculate_discount(total, category)
    return total - discount

consultation = float(input("Enter consultation charges: "))
laboratory = float(input("Enter laboratory charges: "))
medicine = float(input("Enter medicine charges: "))
days = int(input("Enter number of room days: "))
rate = float(input("Enter room charge per day: "))
category = input("Enter patient category (Senior/Student/General): ")

room = room_charges(days, rate)
bill = final_bill(consultation, laboratory, medicine, room, category)

print("Consultation Charges =", consultation)
print("Laboratory Charges =", laboratory)
print("Medicine Charges =", medicine)
print("Room Charges =", room)
print("Final Bill =", bill)