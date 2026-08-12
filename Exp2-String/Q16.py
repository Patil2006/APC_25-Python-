#Display the frequency of every character in a string.

s = input("Enter a string: ")

printed = ""

for i in s:
    if i not in printed:
        count = 0
        for j in s:
            if i == j:
                count += 1
        print(i, "=", count)
        printed += i