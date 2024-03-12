#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
print(f"last digit of {number} is {last} and is", end=" ")
if last > 5:
    print("greater than 5\n")
elif last == 0:
    print("0\n")
else:
    print("less than 6 and not 0\n")
