#!/usr/bin/python3
'''
    Module for function that prints a text with 2 new lines after each of
    these characters: ., ? and :
'''


def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?', and ':'

    :param text: The input text
    :type text: str
    :raises TypeError: If the input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_set = {'.', '?', ':'}
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation_set:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip(), end="")
