# 22. Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average

numbers = list(map(int, input("Enter numbers: ").split()))

minimum, maximum, total, average = calculate(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)