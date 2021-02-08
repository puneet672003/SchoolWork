# write a Python program to generator(Random Number) that generates random  numbers between 1 and 6 (simulates a dice) using user defined function.
import random 

def generator():
    return random.randint(1, 7)

print(generator())