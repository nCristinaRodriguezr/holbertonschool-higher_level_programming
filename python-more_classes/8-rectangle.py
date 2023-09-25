#!/usr/bin/python3
class Rectangle:
    """
    This class aims to create a triangular object and define its width and height,
    as well as multiply the base with the height to get the area of 
    the rectangle and represent the rectangle with #
    Args : width, height
    """
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2