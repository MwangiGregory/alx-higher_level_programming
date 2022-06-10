#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    tuple_list = []
    tuple_list.append(tuple_a)
    tuple_list.append(tuple_b)

    for tp in tuple_list:
        if len(tp) >= 2:
            a += tp[0]
            b += tp[1]
        elif len(tp) == 1:
            a += tp[0]
    return (a, b)
