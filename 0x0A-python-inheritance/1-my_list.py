#!/usr/bin/python3
"""This module defines class MyList"""

class MyList(list):
    """This class inherits from list and add its own
    functionality"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        if None in self:
            raise TypeError('List can only have integers')
        new_list = self[:]
        new_list.sort()
        print(new_list)
