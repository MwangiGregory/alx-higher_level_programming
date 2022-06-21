#!/usr/bin/python3
"""Definition for class Square"""


class Square:
    """Blueprint for a square"""

    def __init__(self, size=0):
        """Initialize the object of Square.

        Ensures size is a positive integer

        Args:
            size (int): The size of the square.
        """
        try:
            if type(size) == int:
                if size >= 0:
                    self.__size = size
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the current square area.

        Return:
            int: The area of the square.
        """

        return (self.__size ** 2)
