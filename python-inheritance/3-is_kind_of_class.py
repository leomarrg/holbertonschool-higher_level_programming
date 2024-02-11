#!/usr/bin/python3
"""
Function that checks if object is an instance of or if
object is instance of a class inherited
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.
   
    Returns:
        True if the object is an instance of, or if the object
        is an instance of a class that inherited from,
        the specified class, otherwise False.
    """
    return isinstance(obj, a_class)
