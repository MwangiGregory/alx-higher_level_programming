#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        if None in self:
            raise TypeError('List can only have integers')
        new_list = self[:]
        new_list.sort()
        print(new_list)
