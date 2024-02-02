#!/usr/bin/python3
"""
Define a class Square
"""


class Square:

    """
    Class that defines a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize new private instance:
            size

        Parameters:
            size
        """
        self.__size = size
        self.position = position

    @property
    def size(self):

        """
        Private instance attribute

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

    @property
    def position(self):
        """
        Private instance attribute

        Returns: tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute

        Parameters:
            Value: (tuple): the position to set

        Raises:
            TypeError:
                if poisition is not a tuple of 2 positive ints
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(num) is int for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
