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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_objs = [obj.to_dictionary() for obj in (list_objs or [])]
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance"""
        if cls.__name__ == 'Rectangle':
            from models.rectangle import Rectangle
            dummy_instance = Rectangle(1, 1)
        elif cls.__name__ == 'Square':
            from models.square import Square
            dummy_instance = Square(1)
        else:
            raise ValueError("Unsupported class")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json', 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        list_dicts = cls.from_json_string(json_string)
        instances = [cls.create(**d) for d in list_dicts]
        return instances

