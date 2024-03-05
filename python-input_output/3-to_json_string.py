#!/usr/bin/python3
import json
"""
a function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    This function return the JSON representation
    """
    json_string = json.dumps(my_obj)
    return json_string
