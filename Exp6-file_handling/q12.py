# Q12. Count how many times each word occurs using a dictionary

file = open("student.txt", "r")

words = file.read().lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word occurrences:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()