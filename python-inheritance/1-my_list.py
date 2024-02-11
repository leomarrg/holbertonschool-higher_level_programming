#!/usr/bin/python3
"""
Class that inherits list type
"""


class MyList(list):
    """
    A class that inherits from the built-in list type.

    Methods:
        print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
