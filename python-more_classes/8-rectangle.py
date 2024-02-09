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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0): 
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

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
            int: The perimeter of the rectangle, or 0 if either the width or height is 0.
        """
        if self.width <= 0 or self.height <= 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """
        Returns a string representation of the rectangle.

        The rectangle is represented by the 'print_symbol' class attribute. If the width or height of the rectangle is 0, an empty string is returned.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (str(self.print_symbol) * self.width + "\n") * self.height
    
    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to recreate the object.

        The string is in the format 'Rectangle(width, height)', where 'width' and 'height' are the width and height of the rectangle, respectively.

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a goodbye message and decrements the class variable 'number_of_instances' when the rectangle is deleted.

        This method is called when the rectangle object is
        about to be destroyed. It prints "Bye rectangle..."
        to the console and decrements the 'number_of_instances'
        class variable by 1 if it's greater than 0.
        """
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1

    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the area of two Rectangle instances and returns the one with the bigger or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the bigger or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
