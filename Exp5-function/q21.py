# 21. Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    if total >= 5000:
        discount = 20
    elif total >= 2000:
        discount = 10
    else:
        discount = 5

    final_bill = total - (total * discount / 100)
    return final_bill

prices = list(map(float, input("Enter item prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))

print("Total Bill =", total_bill(prices, quantities))