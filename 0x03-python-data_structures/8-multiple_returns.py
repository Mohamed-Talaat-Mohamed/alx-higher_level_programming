#!/usr/bin/python3
def multiple_returns(sentence):
    len_gth = len(sentence)
    if len_gth == 0:
        cha = "None"
    else:
        cha = sentence[0]
    operation = (len_gth, cha)
    return (operation)
