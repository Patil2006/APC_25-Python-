tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = ()

for item in tuple1 + tuple2:
    if item not in merged:
        merged += (item,)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Merged tuple without duplicates:", merged)