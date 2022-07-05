#!/usr/bin/python3
"""Definition for function write_file"""


def write_file(filename="", text=""):
    """
    Write a string to text file and returns the
    number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as a_file:
        n = a_file.write(text)
        return n
