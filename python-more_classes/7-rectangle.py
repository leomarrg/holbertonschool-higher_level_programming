#!/usr/bin/python3
"""
Class that defines a rectangle

"""

class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    """
    Private Instance Attribute:
        width: width of rectangle
        height: height of rectangle
    """
    def __init__(self, width=0, height=0): 
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1


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
        else:
            return (str(self.print_symbol) * self.width + "\n") * self.height
    
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
    def __del__(self):
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
