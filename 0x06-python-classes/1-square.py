#!/usr/bin/python3

"""define a class square"""


class Square:
    """non empty square class"""

    def __init__(self, size):
        """initialize a new square
        Args:
            size(int): private size of square
        """
        self.__size = size
