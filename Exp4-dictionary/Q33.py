# 33. Take a string, use a dictionary to find the first character that occurs only once.

string = "swiss"

frequency = {}

for char in string:
    frequency[char] = frequency.get(char, 0) + 1

for char in string:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break