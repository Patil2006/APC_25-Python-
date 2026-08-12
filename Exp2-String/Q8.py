#8.	Frequency of a Character 

s = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency =", count)