#!/usr/bin/python3
for odd in range(0, 10):
    for even in range(0, 10):
        if odd != even and odd < even:
            if odd == 8 and even == 9:
                print(89)
            else:
                print("{}{},".format(odd, even), end=" ")
