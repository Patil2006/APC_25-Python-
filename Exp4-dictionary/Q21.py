# 21. Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.

squares = {}

for i in range(1, 11):
    squares[i] = i * i

print(squares)