#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    if (len(my_list) == 0):
        bool_list.append(False)
    for num in my_list:
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return (bool_list)
