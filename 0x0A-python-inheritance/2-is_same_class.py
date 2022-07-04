#!/usr/bin/python3
"""Definition of function is_same_class()"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly
    an instance of the specified class, otherwise
    it returns false"""

    if type(obj) == a_class and isinstance(obj, a_class):
        return True
    else:
        return False
