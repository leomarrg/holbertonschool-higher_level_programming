#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string).
    
    Args:
        my_obj: The object to convert to a JSON string.
        
    Returns:
        The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
