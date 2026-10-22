# Take a list of words, use filter() and lambda to find words having more than five characters.

words = ["Apple", "Banana", "Computer", "Python", "Programming"]

result = list(filter(lambda word: len(word) > 5, words))

print("Words having more than five characters:", result)