#!/usr/bin/python3
import json
"""
Function that writes an object to a text file
"""

def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation.
    
    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
