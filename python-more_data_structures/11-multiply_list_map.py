#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiply_numbers = map(lambda x: x * number, my_list)
    new_list = list(multiply_numbers)
    return new_list
