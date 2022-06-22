#!/usr/bin/python3
"""Definition for class Square"""


class Square:
    """Blueprint for a square"""

    def __init__(self, size=0):
        """Class constructor"""
        self.size = size

    @property
    def size(self):
        """Retrives value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets and validates assignement to size"""
        try:
            if type(value) == int:
                if value >= 0:
                    self.__size = value
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the current square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square using the # character"""
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
