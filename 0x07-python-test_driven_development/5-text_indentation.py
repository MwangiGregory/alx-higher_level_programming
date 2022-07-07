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
    i = 0
    while i < text_length:
        if i == 0 or i == (text_length - 1):
            if text[i] == " ":
                i += 1
                continue
            else:
                print(text[i], end="")
                i += 1
                continue

        if text[i] in [".", "?", ":"]:
            print("\n")
            i += 1
            while i < text_length and text[i] == " ":
                i += 1
            continue
        else:
            print(text[i], end="")
            i += 1
            continue
