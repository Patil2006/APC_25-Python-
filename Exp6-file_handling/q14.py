# Q14. Replace all occurrences of a specified word with another word

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open("student.txt", "r")

text = file.read()

file.close()

text = text.replace(old_word, new_word)

file = open("student_new.txt", "w")

file.write(text)

file.close()

print("Word replaced successfully.")