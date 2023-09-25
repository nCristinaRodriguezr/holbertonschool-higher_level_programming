#!/usr/bin/python3
class Rectangle:
    """
    This class aims to create a triangular object and define its width and height,
    as well as multiply the base with the height to obtain the area of the rectangle.
    Args: width, height
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

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