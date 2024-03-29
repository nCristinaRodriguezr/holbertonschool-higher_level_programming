#!/usr/bin/python3
"""
Defining a square with some attribute
"""


class Square:
    """
    The objetive of this class is return the square area
    """
    __size = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
