#!/usr/bin/python3
"""
Writes unittest for max_integer
"""
def max_integer(list=[]):
    """
    Parameters:
        list: list received from main
    
    """

    if len(list) == 0:
        return None
    
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]

        i += 1
        
    return result