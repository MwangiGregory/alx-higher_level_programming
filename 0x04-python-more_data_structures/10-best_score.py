#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    max_key = None
    if a_dictionary is not None:
        for key in a_dictionary:
            if (a_dictionary[key] > max):
                max = a_dictionary[key]
                max_key = key
    return (max_key)
