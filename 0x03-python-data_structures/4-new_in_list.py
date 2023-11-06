#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    ne_list = my_list.copy()
    ne_list[idx] = element
    return ne_list
