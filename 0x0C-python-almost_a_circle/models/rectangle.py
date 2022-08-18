#!/usr/bin/python3
"""This module defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """This class defines a new type Rectangle that
    inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for rectangle objects"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Calculate area of a rectangle onject"""
        return self.width * self.height

    def display(self):
        """prints the rectangle shape instance using #
        while also placing the rectangle in the right position
        using the x and y coordinates"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Returns string representation of a rectangle"""

        rect_str = f"[Rectangle] ({self.id}) {self.x}/{self.y}" \
                   f" - {self.width}/{self.height}"
        return rect_str

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y
