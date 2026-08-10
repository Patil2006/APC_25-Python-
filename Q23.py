#23.	Count the frequency of each element in a list.

num = [1, 2, 2, 3, 3, 3, 4, 4]

for i in num:
    count = 0
    for j in num:
        if i == j:
            count += 1
    print(i, "=", count)