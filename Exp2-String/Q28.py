#Count the frequency of every word in a paragraph. 

s = input("Enter a paragraph: ")

words = s.split()
printed = []

for i in words:
    if i not in printed:
        count = 0
        for j in words:
            if i == j:
                count += 1
        print(i, "=", count)
        printed.append(i)
        