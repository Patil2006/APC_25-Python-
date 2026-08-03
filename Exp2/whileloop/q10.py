n = int(input("Enter a number: "))

i = 2
count = 0

while i < n:
    if n % i == 0:
        count = count + 1
    i = i + 1

if count == 0 and n > 1:
    print("Prime Number")
else:
    print("Not a Prime Number")