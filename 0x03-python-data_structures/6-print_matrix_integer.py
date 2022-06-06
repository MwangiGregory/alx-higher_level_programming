#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for i in range(len(lst)):
            print("{:d}".format(lst[i]), end='')
            if (i != (len(lst) - 1)):
                print(" ", end='')
        print()
