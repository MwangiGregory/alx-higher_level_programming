#!/usr/bin/python3
"""This module defines function text_indentation"""


def text_indentation(text):
    """
    This function print a text with 2 new lines after
    each of these characters: '.','?' and ':'.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    text_length = len(text)
    for i in range(text_length):
        if i == 0 or i == (text_length - 1):
            if text[i] == " ":
                continue
            else:
                print(text[i], end="")
                continue
        if text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue
        else:
            print(text[i], end="")

        if text[i] in [".", "?", ":"]:
            print("\n")
