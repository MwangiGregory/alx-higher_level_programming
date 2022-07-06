#!/usr/bin/python3
"""This module defines function load_from_json_file"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON string in a
    JSON file
    """
    with open(filename, 'r', encoding="utf-8") as a_file:
        obj = json.load(a_file)
        return obj
