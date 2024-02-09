#!/usr/bin/python3
import json

"""
Function that returns an object
"""
def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by a JSON string.
    
    Args:
        my_str (str): The JSON string to convert to a Python object.
        
    Returns:
        The Python object represented by my_str.
    """
    return json.loads(my_str)
