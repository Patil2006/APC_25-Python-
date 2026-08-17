# 20. Create a dictionary and display its elements in ascending order of keys.

dict1 = {"c": 30, "a": 10, "b": 20, "e": 50, "d": 40}

for key in sorted(dict1):
    print(key, ":", dict1[key])