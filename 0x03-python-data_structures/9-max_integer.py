#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    ne_list = my_list.copy()
    ne_list.sort()
    return ne_list[-1]
