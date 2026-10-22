# Write a program using functions, map(), filter(), and lambda expressions to process a list of words and:
# a) Find the length of every word.
# b) Extract words having more than five characters.
# c) Sort words according to their length.

def process_words(words):
    lengths = list(map(lambda word: len(word), words))
    long_words = list(filter(lambda word: len(word) > 5, words))
    sorted_words = sorted(words, key=lambda word: len(word))

    print("Length of every word:", lengths)
    print("Words having more than five characters:", long_words)
    print("Words sorted by length:", sorted_words)

words = ["Python", "Java", "Programming", "Code", "Computer", "AI"]

process_words(words)