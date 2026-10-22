# Create a module containing recursive functions for factorial, Fibonacci series, sum of digits, and binary conversion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


def binary_conversion(n):
    if n == 0:
        return ""
    return binary_conversion(n // 2) + str(n % 2)