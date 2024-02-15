#!/usr/bin/python3
class Square:
    """
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def __str__(self):
        printy = []
        if self.__size == 0:
            printy.append("\n")
        else:
            for i in range(self.__position[1]):
                printy.append("\n")
            for i in range(self.__size):
                printy.append("_" * self.__position[0])
                printy.append("#" * self.__size)
                if i != self.size-1:
                    printy.append("\n")
        return "".join(printy)
        

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
        self.__position = value

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
        