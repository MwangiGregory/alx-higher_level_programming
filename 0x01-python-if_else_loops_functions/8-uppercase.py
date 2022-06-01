#!/usr/bin/python3


def uppercase(str):
    s = []

    for c in str:
        i = ord(c)

        if i in range(65, 91):
            s.append(c)
        elif i in range(97, 123):
            i = i - 32
            s.append(chr(i))
        else:
            s.append(c)

    for ch in s:
        print("{}".format(ch), end='')
    print()
