#!/usr/bin/python3
"""
0-rectangle.py
"""


class Rectangle:
    """Defines a rectangular shape"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate then mutate width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve height value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Validate and mutate  height value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate area of the Rectangle"""
        result = self.__height * self.__width
        return result

    def perimeter(self):
        """Calculate perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            result = (self.__width * 2) + (self.__height * 2)
            return result

    def __str__(self):
        """Prints rectangle box"""

        rec_str = ""
        if self.__width == 0 or self.__height == 0:
            return rec_str
        else:
            for h in range(self.__height):
                if self.__height - h == 1:
                    rec_str += "#" * self.__width
                else:
                    rec_str += "#" * self.__width + "\n"
            return rec_str

    def __repr__(self):
        """Provide string equivalent of Rectangle object"""

        rec = "Rectangle({}, {})".format(self.__width, self.__height)
        return rec
