#!/usr/bin/python3
""" defines a square with size"""


class Square:
    """Square Class"""
    def __init__(self, size = 0):
        """Initialize method"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
             raise ValueError('size must be >= 0')
        else:
            self.__size = size
