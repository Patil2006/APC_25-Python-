# 11. Write a function that accepts a string and returns its reverse.

def reverse_string(s):
    return s[::-1]

s = input("Enter a string: ")
print("Reverse =", reverse_string(s))