#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    i = (-number) % 10
    i = -i
else:
    i = number % 10

if i > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, i))
elif i == 0:
    print("Last digit of {} is {} and is 0".format(number, 0))
elif i < 6 and i != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, i))
