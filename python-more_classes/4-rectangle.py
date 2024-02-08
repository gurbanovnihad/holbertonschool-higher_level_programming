#!/usr/bin/python3
'''
    Rectangle Module defines a rectangle
'''


class Rectangle:
    '''
        Rectangle Class
    '''

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __repr__(self):
        module = self.__class__.__module__
        name = self.__class__.__name__
        return "{}({}, {})".format(name, self.width, self.height)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        else:
            square = ""
            for i in range(self.height):
                for j in range(self.width):
                    square += "#"
                    if j == self.width - 1:
                        square += "\n"
            return square[:-1]

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        if self.height != 0 and self.width != 0:
            return self.height * self.width
        else:
            return 0

    def perimeter(self):
        if self.height != 0 and self.width != 0:
            return 2 * (self.height + self.width)
        else:
            return 0
