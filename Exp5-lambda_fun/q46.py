# Take a list of words; sort them according to their length using lambda.

words = ["Python", "AI", "Computer", "Code", "Programming"]

sorted_words = sorted(words, key=lambda x: len(x))

print("Words sorted according to length:")
print(sorted_words)