#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list1 = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return (list1)
    else:
        list1[idx] = element
        return (list1)
