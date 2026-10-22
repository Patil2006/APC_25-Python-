# Accept five numbers from the user, store them in a list, and convert the list into a tuple.

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

numbers = tuple(numbers)

print("Tuple:", numbers)