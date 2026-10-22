#14.	Create a list containing duplicate values and display only unique elements.

num = [1, 2, 2, 3, 4, 4, 5, 5, 6]

unique = []

for i in num:
    if i not in unique:
        unique.append(i)

print("Unique elements =", unique)