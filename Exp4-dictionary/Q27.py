# 27. Create a dictionary containing product names and quantities.
# Perform:
# • Add a product
# • Update quantity
# • Delete a product
# • Search for a product
# • Display products with quantity below 10

products = {
    "Pen": 15,
    "Notebook": 8,
    "Pencil": 20,
    "Eraser": 5
}

products["Bag"] = 12

products["Pen"] = 10

del products["Pencil"]

product = "Notebook"
if product in products:
    print("Product found:", product, products[product])
else:
    print("Product not found")

print("Products with quantity below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, ":", quantity)