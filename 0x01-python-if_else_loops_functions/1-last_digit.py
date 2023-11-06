#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 1:
    o_number = -1 * number
else:
    o_number = number
dig = o_number % 10
if num < 1:
    dig = -dig
if dig == 0:
    print("Last digit of {} is {} and is 0".format(number, gig))
elif dig < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, dig))
else:
    print("Last digit of {} is {} and is greater than 5".format(number, dig))
