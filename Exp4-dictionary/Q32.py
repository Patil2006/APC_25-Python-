# 32. Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for num in numbers:
    complement = target - num

    if complement in seen:
        print("Numbers:", complement, "and", num)
        break

    seen[num] = True