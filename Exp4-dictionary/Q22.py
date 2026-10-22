# 22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.

squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print(squares)