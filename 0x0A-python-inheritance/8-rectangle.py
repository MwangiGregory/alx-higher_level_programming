#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Unimplimented area method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validate value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Class that defines a rectangle"""

    def __init__(self, width, height):
        """Initializer"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
