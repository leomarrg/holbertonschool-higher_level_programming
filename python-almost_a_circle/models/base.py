#!/usr/bin/python3
"""
Defining a class called base
"""
import json


class Base:
    """
    Class that defines a base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new base

        Attributes:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
