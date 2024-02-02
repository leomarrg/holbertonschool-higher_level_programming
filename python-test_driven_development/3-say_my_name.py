#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the provided first and last names.

    Parameters:
        first_name (str): First name.
        last_name (str, optional): Last name, defaults to an empty string.

    Returns:
        None
    """
    # Check if first_name is a string
    if not type(first_name) == str:
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not type(last_name) == str:
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}"
    print(full_name)