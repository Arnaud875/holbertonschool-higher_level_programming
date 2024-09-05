#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print("0 is zero" if number == 0 else "{} is negative".format(number)
      if number < 0 else "{} is positive".format(number))
