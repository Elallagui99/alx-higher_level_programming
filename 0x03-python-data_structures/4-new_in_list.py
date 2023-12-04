#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return (my_list)
        else:
            list1 = my_list.copy()
            list1[idx] = element
            return (list1)
