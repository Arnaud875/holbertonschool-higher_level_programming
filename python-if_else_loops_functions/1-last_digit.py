#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    abs = number * -1
    last = (abs % 10) * -1
else:
    last = number % 10

print(
    "Last digit of {} is 0 and is 0".format(number) if last == 0
    else
    "Last digit of {} is {} and is greater than 5".format(number, last)
    if last > 5
    else
    "Last digit of {} is {} and is less than 6 and not 0".format(number, last))
