#!/usr/bin/python3
"""
This module defines function to_json_string
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation
    of my_obj object
    """
    s = json.dumps(my_obj)
    return s
