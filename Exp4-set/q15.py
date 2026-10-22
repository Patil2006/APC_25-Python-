# 15. Write a program to determine whether two sets have no elements in common.

set1 = {10, 20, 30}
set2 = {40, 50, 60}

result = set1.isdisjoint(set2)

print("Do the sets have no elements in common?", result)