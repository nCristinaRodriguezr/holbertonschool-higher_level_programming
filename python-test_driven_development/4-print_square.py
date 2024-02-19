#!/usr/bin/python3
"""
print square
"""


def print_square(size):
    """
    A function that prints a square with the character #
    Args:
        size (size of square)
    Return:
        print square with #
    Raises:
        TypeError
        ValueError
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, (float)) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for element in range(size):
            print("#"*size)
