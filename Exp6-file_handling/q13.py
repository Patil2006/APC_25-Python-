# Q13. Search for a word and display its occurrences and line numbers

word = input("Enter word to search: ")

file = open("student.txt", "r")

count = 0
line_numbers = []

for line_number, line in enumerate(file, start=1):
    words = line.split()

    for w in words:
        if w.lower() == word.lower():
            count += 1
            line_numbers.append(line_number)

file.close()

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)