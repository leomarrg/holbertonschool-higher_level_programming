#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest_val = -1
    highest_key = 0
    for key, value in a_dictionary.items():
        if value > highest_val:
            highest_val = value
            highest_key = key

    return highest_key
