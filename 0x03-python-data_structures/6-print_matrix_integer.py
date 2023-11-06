#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        counter = 0
        for y in x:
            counter += 1
            print('{:d}'.format(y), end=(" " if counter < len(x) else ""))
        print()
