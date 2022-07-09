#!/usr/bin/python3
"""Defines an empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle and inherits from
    BaseGeometry"""

    def __init__(self, width, height):
        """Initializer"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string description of Rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
