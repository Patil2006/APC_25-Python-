# 11. Create two sets and find:
# Elements present in the first set but not the second
# Elements present in the second set but not the first

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

first_only = set1.difference(set2)
second_only = set2.difference(set1)

print("Elements in first set but not in second:", first_only)
print("Elements in second set but not in first:", second_only)