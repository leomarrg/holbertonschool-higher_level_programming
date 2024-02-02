#!/usr/bin/python3
def print_square(size):
    """
    Prints a square using the character '#'.

    Parameters:
        size: size of square

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)