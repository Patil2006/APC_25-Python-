# Import functions from texttools package.

from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter text: ")

cleaned_text = remove_punctuation(text)
cleaned_text = remove_extra_spaces(cleaned_text)

print("\nCleaned Text:", cleaned_text)
print("Tokens:", tokenize(cleaned_text))
print("Word Frequency:", word_frequency(cleaned_text))