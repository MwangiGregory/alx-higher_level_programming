#!/usr/bin/python3
"""
This module defines function append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as a_file:
        n = a_file.write(text)
        return n
