#!/usr/bin/python3
""""
Loads data from a json file and returns object
"""
import json

def load_from_json_file(filename):
    """
    Loads data from a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON data.

    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
