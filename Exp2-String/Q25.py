#Find the second most frequently occurring character. 

s = input("Enter a string: ")

first = second = 0
fchar = schar = ""

for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1

    if count > first and i != fchar:
        second = first
        schar = fchar
        first = count
        fchar = i
    elif count > second and count < first and i != schar:
        second = count
        schar = i

print("Second highest frequency character =", schar)
print("Frequency =", second)