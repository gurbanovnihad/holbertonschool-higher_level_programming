#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return

    best_score = 0
    item_key = ''

    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            item_key = key
    return item_key
