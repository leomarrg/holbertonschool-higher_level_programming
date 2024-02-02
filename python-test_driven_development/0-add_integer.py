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
    if (type(a) not in (int, float)):
        raise TypeError("a must be an integer")
    
    if(type(b) not in (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    result = a + b
    return result
