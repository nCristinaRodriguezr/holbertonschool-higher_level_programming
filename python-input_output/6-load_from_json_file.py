#!/usr/bin/python3
import json
"""
A function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
    Create an object from a JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
