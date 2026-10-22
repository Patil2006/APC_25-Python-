# Q11. Read a text file and find the longest word

file = open("student.txt", "r")

words = file.read().split()

longest = max(words, key=len)

print("Longest word:", longest)
print("Length:", len(longest))

file.close()