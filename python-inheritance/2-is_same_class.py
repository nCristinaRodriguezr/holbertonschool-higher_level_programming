#!/usr/bin/python3
"""
A function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""

def is_same_class(obj, a_class):
    """
    Verify if the object is the same object of the class
    """
    return isinstance(obj, a_class)
