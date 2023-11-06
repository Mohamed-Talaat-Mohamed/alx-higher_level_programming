#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for s in my_string:
        if s != 'c' and s != 'C':
            n_str += s
    return n_str
