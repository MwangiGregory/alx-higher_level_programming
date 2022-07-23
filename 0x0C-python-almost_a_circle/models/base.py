#!/usr/bin/python3
""" This module defines class Base"""


class Base:
    """ This class defines object of type Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for objects of type Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
