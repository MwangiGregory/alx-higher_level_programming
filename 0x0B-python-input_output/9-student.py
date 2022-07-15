#!/usr/bin/python3
"""This module defines class student"""


class Student:
    """This class defines a student type"""
    def __init__(self, first_name, last_name, age):
        """Initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Serializes an object of type Student"""
        return self.__dict__
