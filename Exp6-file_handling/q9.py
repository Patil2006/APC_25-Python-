# Q9. Count the number of vowels and consonants in a text file

file = open("student.txt", "r")

text = file.read()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

file.close()