#!/usr/bin/python3
"""
Class Base geometry
"""


class BaseGeometry:
    """
    Represents BaseGeometry.
    """
    
    def area(self):
        """
        Public instance method that calculates the area.
        Raises:
            Exception: Always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
