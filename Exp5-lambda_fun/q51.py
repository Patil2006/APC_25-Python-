# Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
# a) Calculate total value of each product.
# b) Filter products costing more than ₹1,000.
# c) Sort products according to total value.

def process_products(products):
    for product in products:
        product["total"] = product["price"] * product["quantity"]

    expensive = list(filter(lambda p: p["total"] > 1000, products))
    sorted_products = sorted(products, key=lambda p: p["total"])

    print("Total value of each product:")
    for p in products:
        print(p["name"], ":", p["total"])

    print("\nProducts costing more than ₹1,000:")
    for p in expensive:
        print(p["name"])

    print("\nProducts sorted by total value:")
    for p in sorted_products:
        print(p["name"], ":", p["total"])


products = [
    {"name": "Laptop", "price": 50000, "quantity": 2},
    {"name": "Mouse", "price": 500, "quantity": 1},
    {"name": "Keyboard", "price": 1500, "quantity": 2},
    {"name": "Headphones", "price": 2000, "quantity": 1}
]

process_products(products)