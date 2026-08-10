#25.	Remove all duplicate elements while preserving the original order.

num = [1, 2, 2, 3, 4, 4, 5, 1]

unique = []

for i in num:
    if i not in unique:
        unique.append(i)

print("List without duplicates =", unique)