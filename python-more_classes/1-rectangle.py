#!/usr/bin/python3
"""
Class that defines a rectangle

"""

class Rectangle:
    """
    Represents a rectangle
    Private Instance Attribute:
        width: width of rectangle
        height: height of rectangle
    """
    def __init__(self, width=0, height=0): 
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        The width getter.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        The width setter.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    @property
    def height(self):
        """
        The height getter.

        Returns:
            int: The height of the rectangle.
        """
        return self._height
    
    @height.setter
    def height(self, value):
        """
        The height setter.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
