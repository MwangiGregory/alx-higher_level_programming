#!/usr/bin/python3
"""Definition of function read_file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
