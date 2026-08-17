# 24. Store visitor IDs from two different days in separate sets. Determine:
# Unique visitors across both days
# Returning visitors
# Visitors who came only on the first day
# Visitors who came only on the second day
# Create sets representing products belonging to different categories. Find products that belong to both categories.

day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {103, 104, 105, 106, 107}

unique_visitors = day1_visitors.union(day2_visitors)
returning_visitors = day1_visitors.intersection(day2_visitors)
only_day1 = day1_visitors.difference(day2_visitors)
only_day2 = day2_visitors.difference(day1_visitors)

print("Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on the first day:", only_day1)
print("Visitors only on the second day:", only_day2)

electronics = {"Laptop", "Mobile", "Headphones", "Smartwatch"}
accessories = {"Mobile", "Headphones", "Charger", "Mouse"}

common_products = electronics.intersection(accessories)

print("Products belonging to both categories:", common_products)