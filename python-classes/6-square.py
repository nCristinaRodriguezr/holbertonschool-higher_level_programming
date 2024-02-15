#!/usr/bin/python3
class Square:
    """
    The objective of this class is to learn how to assign a method that changes a private attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @position.setter
    def position(self, value):
        if not (value[0] >= 0 and value[1] >= 0 and isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__positionposition = value

    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("_" * self.__position[0], end="")
                print("#" * self.__size)