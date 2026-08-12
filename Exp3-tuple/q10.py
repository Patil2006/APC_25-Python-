# Create a tuple of 10 numbers and display:
# First five elements
# Last five elements
# Middle four elements
# Alternate elements
# Reverse tuple

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("First five elements:", numbers[:5])
print("Last five elements:", numbers[5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])