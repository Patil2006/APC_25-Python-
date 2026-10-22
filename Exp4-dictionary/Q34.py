# 34. Take a string, use a dictionary to find the first character that occurs more than once.

string = "programming"

frequency = {}

for char in string:
    frequency[char] = frequency.get(char, 0) + 1

for char in string:
    if frequency[char] > 1:
        print("First repeating character:", char)
        break