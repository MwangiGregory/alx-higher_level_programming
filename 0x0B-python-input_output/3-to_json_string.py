#!/usr/bin/python3
import json
"""
This module defines function to_json_string
"""


def to_json_string(my_obj):
    """
    This function returns the JSON representation
    of my_obj object
    """
    s = json.dumps(my_obj)
    return s
