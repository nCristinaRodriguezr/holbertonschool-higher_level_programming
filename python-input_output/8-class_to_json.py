#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Convert an instance of a class to a serializable dictionary in JSON
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("The object is not serializable.\
                         Make sure it is an instance of a class.")
    serializable_attributes = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value
    return serializable_attributes
