# Accept a string from the user and create a dictionary containing each character and its frequency.

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)