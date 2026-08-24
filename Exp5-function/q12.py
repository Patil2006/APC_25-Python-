# 12. Create a function that checks whether a given string or number is a palindrome.

def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

value = input("Enter a string or number: ")

print(is_palindrome(value))