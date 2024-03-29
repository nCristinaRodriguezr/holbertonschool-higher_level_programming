#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


class Rectangle(BaseGeometry):
    """
    This class inheritance of BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
