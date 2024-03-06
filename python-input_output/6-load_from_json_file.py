#!/usr/bin/python3
import json
from os.path import exists
"""
A function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
    Create an object from a JSON file.
    """
    if exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []
