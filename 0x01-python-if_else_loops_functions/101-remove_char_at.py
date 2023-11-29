#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(str):
        if i != n:
            str1 = str[i]
    print("{}".format(str1), end="")
