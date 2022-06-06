#!/usr/bin/python3
def no_c(my_string):
    st = ""
    for ch in my_string:
        if (ch == "c" or ch == "C"):
            continue
        else:
            st += ch
    return st
