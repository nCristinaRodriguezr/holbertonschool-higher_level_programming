#!/usr/bin/python3
import json
"""
A function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """
    Converts a JSON string to a Python data structure.
    """
    python_object = json.loads(my_str)
    return python_object
