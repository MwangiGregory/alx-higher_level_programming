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

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionaries from json string
        representation of a list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            list_dicts = json.loads(json_string)
            return list_dicts

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 2)  # dummy attributes
        elif cls.__name__ == "Square":
            obj = cls(1)  # dummy attributes
        obj.update(**dictionary)
        return obj

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of a list of objects to a file"""

        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
