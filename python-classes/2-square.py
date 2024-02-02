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

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
