#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each . ? :

    Parameters:
        text: string 
    
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
