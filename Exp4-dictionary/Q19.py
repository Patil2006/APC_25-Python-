# 19. Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.

dict1 = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}

result = {}

for key, value in dict1.items():
    if value not in result.values():
        result[key] = value

print("Original dictionary:", dict1)
print("Dictionary after removing duplicates:", result)