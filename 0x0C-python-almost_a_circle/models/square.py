#!/usr/bin/python3
"""This module defines class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intializer"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of a Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns an argument to each field of Square"""
        if args is not None and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if id is not None:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                elif key == "size":
                    self.size = arg
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
