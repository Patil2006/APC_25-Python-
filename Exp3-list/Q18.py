"""18.	Create a shopping cart using a list.
Perform:
•	Add item 
•	Remove item 
•	Search item 
•	Display cart 
•	Count total items"""

cart = []

cart.append("Apple")
cart.append("Milk")
cart.append("Bread")

cart.remove("Milk")

if "Apple" in cart:
    print("Item found")
else:
    print("Item not found")

print("Cart =", cart)
print("Total items =", len(cart))