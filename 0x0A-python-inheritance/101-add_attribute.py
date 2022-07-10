#!/usr/bin/python3
"""This module defines function add_attribute"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
