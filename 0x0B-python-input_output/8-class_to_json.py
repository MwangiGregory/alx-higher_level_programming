#!/usr/bin/python3
"""This module defines function class_to_json"""


def class_to_json(obj):
    """
    This function returns the dictionary description
    of an object for JSON serialization of the Object
    """
    return obj.__dict__
