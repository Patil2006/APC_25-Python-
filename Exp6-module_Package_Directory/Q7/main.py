# Import functions from mathutils package.

from mathutils.basic import addition, subtraction, multiplication, division
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

numbers = [a, b]

print("\nArithmetic Operations")
print("Addition:", addition(a, b))
print("Subtraction:", subtraction(a, b))
print("Multiplication:", multiplication(a, b))
print("Division:", division(a, b))

print("\nNumber Operations")
print("Prime:", is_prime(a))
print("Armstrong:", is_armstrong(a))
print("Palindrome:", is_palindrome(a))

print("\nStatistical Operations")
print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))