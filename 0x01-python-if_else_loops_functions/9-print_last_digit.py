#!/usr/bin/python3


def print_last_digit(number):
    status = True
    rem = 0

    if (number < 0):
        number = number * -1
    while status:
        rem = number % 10

        if rem in range(0, 10):
            print("{:d}".format(rem), end='')
            break

    return rem
