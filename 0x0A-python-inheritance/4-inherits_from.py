#!/usr/bin/python3
"""Defines function inherits_from"""


def inherits_from(obj, a_class):
    """
    Checks if object obj is an instance of a class that
    inherits(directly or indirectly) from the specified
    class a_class
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
