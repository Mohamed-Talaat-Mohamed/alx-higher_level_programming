#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 1:
    o_num = -1 * num
else:
    o_num = num
dig = o_num % 10
if num < 1:
    dig = -dig
if dig == 0:
    print("Last digit of {} is {} and is 0".format(num, gig))
elif dig < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, dig))
else:
    print("Last digit of {} is {} and is greater than 5".format(num, dig))
