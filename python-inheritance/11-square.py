#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
A class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""


class Square(Rectangle):
    """
    This class inheritance of class Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
