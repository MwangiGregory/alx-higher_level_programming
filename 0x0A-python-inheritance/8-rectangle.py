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
