#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ne_args = len(sys.argv) - 1
    if ne_args == 0:
        print("0 arguments.")
    elif ne_args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(ne_args))
        for x in range(ne_args):
            print("{}: {}".format(x + 1, sys.argv[x + 1]))
