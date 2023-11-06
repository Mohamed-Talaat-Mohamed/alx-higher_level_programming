#!/usr/bin/python3
def print_last_digit(number):
    if number < 1:
        number = -1 * number
    dig = number % 10
    if number < 1:
        dig = -1 * dig
    print(dig, end="")
    return dig
