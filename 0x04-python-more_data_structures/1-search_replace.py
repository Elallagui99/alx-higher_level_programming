#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = my_list.copy()
    for element in new:
        if element == search:
            new[element] = replace
    return (new)
