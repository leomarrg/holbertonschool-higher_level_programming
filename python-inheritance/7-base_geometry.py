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
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
