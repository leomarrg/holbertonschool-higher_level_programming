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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self._width = value

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either
            the width or height is 0.
        """
        if self.width <= 0 or self.height <= 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        The rectangle is represented by the '#' character. If the
        width or height of the rectangle is 0, an empty string is
        returned.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle_str += "#"
            rectangle_str += "\n"
        return rectangle_str
