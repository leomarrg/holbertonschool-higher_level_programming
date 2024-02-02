#!/usr/bin/python3
"""
Function that adds two intefers
"""
def add_integer(a, b=98):
    """
    Parameters:
        a
        b by default is 98

    Returns:
        sum of a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    result = a + b
    return result
