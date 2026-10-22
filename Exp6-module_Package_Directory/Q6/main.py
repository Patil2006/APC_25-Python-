# Import and use recursive functions from recursive_utils module.

from recursive_utils import factorial, fibonacci, sum_of_digits, binary_conversion

num = int(input("Enter a number: "))

print("Factorial:", factorial(num))

print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacci(i), end=" ")

print("\nSum of digits:", sum_of_digits(num))

if num == 0:
    print("Binary:", 0)
else:
    print("Binary:", binary_conversion(num))