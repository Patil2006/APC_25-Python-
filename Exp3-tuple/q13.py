# Modify a tuple by converting it into a list and then back into a tuple.

numbers = (10, 20, 30, 40, 50)

numbers_list = list(numbers)
numbers_list[2] = 100

numbers = tuple(numbers_list)

print("Modified tuple:", numbers)