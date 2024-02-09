#!/usr/bin/python3
def lookup(obj):
    """
    Function to return the list of available attributes and methods of an object.
    
    Args:
        obj: The object whose attributes and methods are to be returned.
        
    Returns:
        A list of attributes and methods of the object.
    """
    return dir(obj)