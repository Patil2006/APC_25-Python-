# Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.

list1 = [10, 20, 30, 40]
list2 = [5, 15, 25, 35]

result = list(map(lambda x, y: x + y, list1, list2))

print("Sum of corresponding elements:", result)