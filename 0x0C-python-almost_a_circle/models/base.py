#!/usr/bin/python3
""" This module defines class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)
