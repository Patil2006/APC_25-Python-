# Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)