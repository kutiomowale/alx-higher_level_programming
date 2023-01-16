#!/usr/bin/python3

"""Text indentation
A function that prints a text with 2 new lines after each of these characters:
., ? and :
"""


def text_indentation(text):
    """Text indentation

    A function that prints a text with 2 new lines after
    each of these characters: '.', '?' and ':'

    Args:
        text (str) : The text to print

    Raises:
        TypeError: If text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if len(text) == 0:
        return
    text_list = [char for char in text]
    buff = []
    for char in text_list:
        buff.append(char)
        if char in ['.', '?', ':']:
            text_to_print = ''.join(buff)
            text_to_print = text_to_print.strip()
            print(text_to_print)
            print()
            buff.clear()
    if len(buff) != 0:
        text_to_print = ''.join(buff)
        text_to_print = text_to_print.strip()
        print(text_to_print, end='')
