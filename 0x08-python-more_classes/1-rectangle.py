#!/usr/bin/python3
""" 0-rectangle.py """


class Rectangle:
    """Defines a rectangular shape"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle object
        Args:
            self.width(int): integer
            self.height(int): integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate then mutate width value"""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        """Retrieve height value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Validate and mutate  height value"""

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
