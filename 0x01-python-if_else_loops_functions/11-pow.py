#!/usr/bin/python3


def pow(a, b):
    a = float(a)
    if (b == 0):
        return 1
    elif (b == 1):
        return a
    elif (b < 0):
        return ((1 / a) * pow(a, b + 1))
    else:
        return a * pow(a, b - 1)
