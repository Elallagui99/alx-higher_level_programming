#!/user/bin/python3

"""define a class square"""


class Square:
    """non empty square class"""

    def __init__(self, size=0):
        """initialize a new square
        Args:
        size(int): private size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """instance method return square area"""
        return (self.__size * self.__size)
