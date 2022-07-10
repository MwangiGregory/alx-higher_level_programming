#!/usr/bin/python3
"""
This module defines a script that adds
command line arguments to a python list, and then
saves them to a file
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
contents = []

try:
    contents = load_from_json_file(filename)
except FileNotFoundError:
    save_to_json_file(contents, filename)

contents += argv[1:]
save_to_json_file(contents, filename)
