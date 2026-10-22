# 17. Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))
print("Fibonacci numbers =", fibonacci(n))