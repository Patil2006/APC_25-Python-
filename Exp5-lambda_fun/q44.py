# Take a list of numbers, use filter() and lambda to find numbers greater than 50.

numbers = [20, 45, 60, 75, 30, 90, 50]

result = list(filter(lambda x: x > 50, numbers))

print("Numbers greater than 50:", result)