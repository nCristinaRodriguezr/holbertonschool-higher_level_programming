#!/usr/bin/python3
"""
defining the class a square
"""


class Square:
    """
    The objetive of this class is learning to use methods.
    """
    __size = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
