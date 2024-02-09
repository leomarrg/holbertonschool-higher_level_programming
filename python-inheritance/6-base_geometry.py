#!/usr/bin/python3
class BaseGeometry:
    """
    A class named BaseGeometry.
    """
    
    def area(self):
        """
        Public instance method that calculates the area.
        Raises:
            Exception: Always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
