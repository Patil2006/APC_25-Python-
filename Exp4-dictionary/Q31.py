# 31. Take a list of words, create a dictionary where the key is the word length
# and the value is a list of words having that length.

words = ["cat", "dog", "apple", "ball", "sun", "orange"]

result = {}

for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print(result)