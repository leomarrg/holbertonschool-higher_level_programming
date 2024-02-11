#!/usr/bin/python3
"""
Function that returns dict descriptcion
"""


def class_to_json(obj):
    """
    Function that returns a dict description
    with simple data structure (list, dict, string, int, bool)
    """

    return obj.__dict__
