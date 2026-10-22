# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.

def count_element(items, element):
    count = 0
    for item in items:
        if item == element:
            count += 1
    return count

items = input("Enter list elements: ").split()
element = input("Enter element to count: ")

print("Number of occurrences =", count_element(items, element))