#!/usr/bin/python3
"""
0-rectangle.py
"""


class Rectangle:
    """Defines a rectangular shape"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            st = str(self.print_symbol) * self.__width
            for h in range(self.__height):
                if self.__height - h == 1:
                    rec_str += "{}".format(st)
                else:
                    rec_str += "{}\n".format(st)
            return rec_str

    def __repr__(self):
        """Provide string equivalent of Rectangle object"""

        rec = "Rectangle({}, {})".format(self.__width, self.__height)
        return rec

    def __del__(self):
        """Deleter"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            area_1 = rect_1.area()
            area_2 = rect_2.area()
            if area_1 > area_2:
                return rect_1
            elif area_2 > area_1:
                return rect_2
            else:
                return rect_1
