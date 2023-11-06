#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ne_list = []
    for item in my_list:
        if (item % 2) == 0:
            ne_list.append(True)
        else:
            ne_list.append(False)
    return ne_list
