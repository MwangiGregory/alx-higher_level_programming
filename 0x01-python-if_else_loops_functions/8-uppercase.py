#!/usr/bin/python3


def uppercase(str):
    for c in str:
        i = ord(c)

        '#check if uppercase'
        if i in range(65, 91):
            print("{:c}".format(i), end='')
        elif i in range(97, 123):
            i = i - 32
            print("{:c}".format(i), end='')
        else:
            print("{:c}".format(i), end='')
    print()
