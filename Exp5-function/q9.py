# 9. Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.

def largest_number(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = list(map(int, input("Enter numbers: ").split()))

print("Largest element =", largest_number(numbers))