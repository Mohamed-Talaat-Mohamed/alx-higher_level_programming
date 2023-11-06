#!/usr/bin/python3
def print_last_digit(number):
    if number < 1:
    l_d = abs(number) % 10
    if number < 1:
        l_d = abs(l_d)
    print(l_d, end="")
    return l_d
