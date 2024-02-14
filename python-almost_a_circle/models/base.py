#!/usr/bin/python3
"""
Defining a class called base
"""

class Base:
    """
    Class that defines a base

    Attributes:
        id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
