#!/usr/bin/python3
"""
Function that appends a string
"""
def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
    
    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
        
    Returns:
        The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
