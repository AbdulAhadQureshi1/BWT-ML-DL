import random

def random_number_generator(start, end, count=10):
    for _ in range(count):
        yield random.randint(start, end)