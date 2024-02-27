#!/usr/bin/python3
"""
A function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    dir will return a list that includes all the
    attributes and methods of the object
    """
    return dir(obj)
