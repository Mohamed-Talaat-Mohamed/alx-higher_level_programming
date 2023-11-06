#!/usr/bin/python3
alphabet = ord('z')
while alphabet >= ord('a'):
    if alphabet % 2 == 0:
        print("{:c}".format(alphabet), end='')
    else:
        print("{:c}".format(alphabet - (ord('a') - ord('A'))), end='')
    alphabet -= 1
