#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    ne_str = ""
    for cha in str:
        if x == n:
            pass
        else:
            ne_str += cha
        x += 1
    return ne_str
