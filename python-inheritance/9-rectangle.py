#!/usr/bin/python3
"""
Class Base geometry
"""


class BaseGeometry:
    """
    A class represents BaseGeometry.
    """
    
    def area(self):
        """
        Public instance method that calculates the area.
        Raises:
            Exception: Always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """
        Public instance method that validates value.
        
        Args:
            name (str): The name of the value.
            value (int): The value to validate.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""
Class rectanlge
"""

class Rectangle(BaseGeometry):
    """
    A class named Rectangle that inherits from BaseGeometry.
    """
    
    def __init__(self, width, height):
        """
        Instantiates a Rectangle object.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        
        Returns:
            A string in the format '[Rectangle] <width>/<height>'.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
