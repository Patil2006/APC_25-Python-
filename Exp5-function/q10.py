# 10. Define a function that accepts a string and returns the number of vowels present in it.

def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels =", count_vowels(s))