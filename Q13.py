"""13.	Accept 10 numbers and sort them in:
•	Ascending order 
•	Descending order"""

num = []

for i in range(10):
    n = int(input("Enter number: "))
    num.append(n)

print("Ascending =", sorted(num))
print("Descending =", sorted(num, reverse=True))