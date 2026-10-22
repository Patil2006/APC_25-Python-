# 35. Accept a paragraph and create a dictionary where:
# • Key = word length
# • Value = number of words having that length.

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
result = {}

for word in words:
    length = len(word)

    if length in result:
        result[length] += 1
    else:
        result[length] = 1

print("Word length frequency:", result)