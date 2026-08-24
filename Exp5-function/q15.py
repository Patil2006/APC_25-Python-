# 15. Write a function that accepts a list and returns a new list containing only unique elements.

def unique_elements(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

items = input("Enter list elements: ").split()

print("Unique elements =", unique_elements(items))