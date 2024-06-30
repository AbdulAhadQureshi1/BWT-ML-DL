from countdown import Countdown
from fibonacci import fibonacci_generator
from random_num_generator import random_number_generator

# Demonstrating the Countdown iterator
print("Countdown from 10 to 1:")
countdown = Countdown(10)
for i in countdown:
    print(i, end=", ")

# Demonstrating the fibonacci_generator
limit = 10
print(f"\nFibonacci series up to {limit}:")
for num in fibonacci_generator(limit):
    print(num, end=", ")

# Demonstrating the random_number_generator
start = 1
end = 50
print (f"\nRandom numbers between {start} and {end}:")
for num in random_number_generator(start, end):
    print(num, end=", ")
