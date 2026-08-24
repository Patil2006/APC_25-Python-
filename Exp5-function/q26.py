# 26. Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.

def calculate_energy_charge(units):
    if units <= 100:
        charge = units * 5
    elif units <= 200:
        charge = (100 * 5) + ((units - 100) * 7)
    else:
        charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return charge

def calculate_discount(amount):
    if amount >= 3000:
        return amount * 0.10
    elif amount >= 2000:
        return amount * 0.05
    else:
        return 0

def calculate_bill(units):
    fixed_charge = 100
    energy_charge = calculate_energy_charge(units)

    subtotal = energy_charge + fixed_charge
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = taxable_amount * 0.05

    final_bill = taxable_amount + tax

    return energy_charge, fixed_charge, discount, tax, final_bill

units = int(input("Enter electricity units consumed: "))

energy, fixed, discount, tax, bill = calculate_bill(units)

print("Energy Charge =", energy)
print("Fixed Charge =", fixed)
print("Discount =", discount)
print("Tax =", tax)
print("Final Electricity Bill =", bill)