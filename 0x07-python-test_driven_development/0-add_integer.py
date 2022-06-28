#!/usr/bin/python3
""" Definition of function add_integer

The function performs addition operation between
two values. The values can either be floats or integers.
"""

def add_integer(a, b=98):
    """Adds two numbers

    Args:
        a (:obj:`int`, `float`): Must be an integer or float value
        b (:obj:`int`, `float`, optional): Must be an integer or float value.

    Returns:
        int: Sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
