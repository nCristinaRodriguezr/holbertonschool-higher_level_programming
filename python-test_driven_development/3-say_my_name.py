#!/usr/bin/python3
"""
print many names
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints My name is <first name> <last name>.
    Args:
        first_name
        last_name
    Return:
        A full name
    Raises:
        TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
