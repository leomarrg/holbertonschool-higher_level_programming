#!/usr/bin/python3
"""
Prints a text with 2 new lines after each . ? :
"""
def text_indentation(text):
    """
    Parameters:
        text: string 

    Raises:
        TyperError
        ValueError

    Returns:
        Nothing
    """
    punctuations = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuations:
            print(current_line.strip() + '\n')
            current_line = ""

    if current_line:
        print(current_line.strip())
