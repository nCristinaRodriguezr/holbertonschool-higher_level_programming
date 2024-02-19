#!/usr/bin/python3
"""
print de strings
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after each
    of these characters: ., ? and :
    Args:
        text
    Return:
        the string
    Raises:
        TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i, char in enumerate(text):
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
        elif char == ' ' and text[i-1] in (".", "?", ":"):
            pass
        else:
            print(char, end="")
