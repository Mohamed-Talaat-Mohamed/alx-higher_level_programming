#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    ne_args = len(sys.argv) - 1
    for x in range(ne_args):
        total += int(sys.argv[x + 1])
    print(total)
