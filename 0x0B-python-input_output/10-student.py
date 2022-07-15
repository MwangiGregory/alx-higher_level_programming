#!/usr/bin/python3
"""This module defines class student"""


class Student:
    """This class defines a student type"""
    def __init__(self, first_name, last_name, age):
        """Initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Serializes an object of type Student"""
        if type(attrs) is list:
            filtered = {}
            current_dict = self.__dict__
            for attr in current_dict:
                if attr in attrs:
                    filtered[attr] = current_dict[attr]
                    return filtered
        else:
            return self.__dict__
