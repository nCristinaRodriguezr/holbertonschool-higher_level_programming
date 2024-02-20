#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
"""


class Rectangle:
    """
    This class aims to create a triangular
    object and define its width and height,
    as well as multiply the base with the
    height to get the area of the rectangle
    and represent the rectangle with #
    Args : width, height
    """
    def __init__(self, width=0, height=0):
        self.__height = 0
        self.__width = 0
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an intege")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return None
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str = rectangle_str + "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
