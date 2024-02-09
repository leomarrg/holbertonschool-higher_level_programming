#!/usr/bin/python3
"""
Class that defines a rectangle

"""

class Rectangle:
    """
    Private Instance Attribute:
        width: width of rectangle
        height: height of rectangle
    """
    def __init__(self, width=0, height=0): 
        self._width = width
        self._height = height


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self.width * self.height
    def perimeter(self):
        if self.width <= 0 or self.height <= 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
                for j in range(self.width):
                    rectangle_str += "#"
                rectangle_str += "\n"
        return rectangle_str
