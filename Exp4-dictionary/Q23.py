# 23. Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [10, 20, 10, 30, 20, 10, 40, 30]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)