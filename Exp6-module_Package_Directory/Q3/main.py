# Import the required functions into the main program.

from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

num = int(input("Enter a number: "))

print("Prime:", is_prime(num))
print("Palindrome:", is_palindrome(num))
print("Armstrong:", is_armstrong(num))
print("Perfect:", is_perfect(num))