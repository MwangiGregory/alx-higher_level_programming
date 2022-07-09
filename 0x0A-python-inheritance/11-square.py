#!/usr/bin/python3
"""This module defines class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square"""

    def __init__(self, size):
        """Initializer"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of a Square"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
