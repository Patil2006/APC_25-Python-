#Find the character with the highest frequency. 

s = input("Enter a string: ")

max_count = 0
max_char = ""

for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        max_char = i

print("Highest frequency character =", max_char)
print("Frequency =", max_count)