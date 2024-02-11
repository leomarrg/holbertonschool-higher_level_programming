#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.
    
    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
