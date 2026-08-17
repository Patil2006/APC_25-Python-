# 18. Accept a sentence from the user and use a set to display all unique words.

sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words:", words)