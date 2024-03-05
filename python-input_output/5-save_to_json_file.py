#!/usr/bin/python3
import json
"""
A function that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)
