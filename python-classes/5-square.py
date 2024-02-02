#!/usr/bin/python3
"""
Define a class Square
"""
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
        Returns size of square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Setter for size attribute

        Parameters:
            value: size to set
        Raises:
            TypeError: size must be int
            ValueError: size cannot be less than 0
        """

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

    def my_print(self):
        """
        Prints the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)