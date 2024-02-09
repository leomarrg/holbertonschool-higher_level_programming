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
