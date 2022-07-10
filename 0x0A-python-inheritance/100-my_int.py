#!/usr/bin/python3
"""This module defines class MyInt"""


class MyInt(int):
    """Definition of class MyInt which inherits from int"""
    def __eq__(self, int2):
        """Returns false if self == int2"""
        return False

    def __ne__(self, int2):
        """Returns True if self =! int2"""
        return True
