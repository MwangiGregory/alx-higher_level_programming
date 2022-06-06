#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = 0
    my_list_len = len(my_list)
    if my_list:
        if my_list_len == 0:
            return None

        for i in range(0, my_list_len):
            if my_list[i] > mx:
                mx = my_list[i]
    else:
        return None
    return mx
