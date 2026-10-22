n = int(input("Enter number: "))
r = int(n ** 0.5)

for i in range(2, r):
    if r % i == 0:
        print("Square root is not prime")
        break
else:
    print("Square root is prime")