#!/usr/bin/python3
class Square:

    """
    Class that defines a square    
    
    """
    def __init__(self, size=0):
        """
        Initialize new private instance:
            size

        Parameters:
            size
        """
        self.__size = size
    @property
    def size(self):
        """
        Getter method for size attribute

        Returns size of square
        """
        return self.__size
    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of a square
        """
        return self.__size * self.__size