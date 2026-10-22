# Q6. Count the total number of words in a text file
file = open("student.txt", "r")
text = file.read()
words = text.split()
print("Total number of words:", len(words))
file.close()