#!/usr/bin/python3
"""Definition for class Square"""


class Square:
    """Blueprint for a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Class constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrives the coordinates of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets and validates the value of position"""
        try:
            if len(value) == 2:
                if type(value[0]) == int and type(value[1]) == int:
                    self.__position = value
                else:
                    raise TypeError
            else:
                raise TypeError
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of the current square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square using the # character"""
        if (self.__size == 0):
            print()
        for y in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            print()
