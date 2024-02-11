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

    def to_json(obj):
        """
        Function that returns a dict description
        with simple data structure (list, dict, string, int, bool)
        """

        return obj.__dict__
