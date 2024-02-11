#!/usr/bin/python3
"""
Class that defines a students
"""
class Student:
    """
    This class defines a student with first_name,
    last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that returns a dict description
        with simple data structure (list, dict, string, int, bool)
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict