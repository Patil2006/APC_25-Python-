# 28. Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.

products = {}

def add_product(name, price, quantity):
    products[name] = {"price": price, "quantity": quantity}

def remove_product(name):
    if name in products:
        del products[name]
        print("Product removed successfully.")
    else:
        print("Product not found.")

def calculate_subtotal():
    subtotal = 0
    for product in products.values():
        subtotal += product["price"] * product["quantity"]
    return subtotal

def apply_coupon(subtotal, coupon):
    if coupon == "SAVE10":
        return subtotal * 0.10
    elif coupon == "SAVE20":
        return subtotal * 0.20
    else:
        return 0

def calculate_gst(amount):
    return amount * 0.18

def generate_invoice(coupon):
    subtotal = calculate_subtotal()
    discount = apply_coupon(subtotal, coupon)
    amount = subtotal - discount
    gst = calculate_gst(amount)
    final_amount = amount + gst

    print("\n----- FINAL INVOICE -----")
    for name, product in products.items():
        total = product["price"] * product["quantity"]
        print(name, "=", total)

    print("Subtotal =", subtotal)
    print("Discount =", discount)
    print("GST =", gst)
    print("Final Amount =", final_amount)

add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
add_product("Keyboard", 2000, 1)

coupon = input("Enter coupon code: ")

generate_invoice(coupon)