#!/usr/bin/python3
'''Square module'''


class Square:
    '''Square class'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, position):
        self.__position = position

        if not (isinstance(self.__position, tuple)) or len(position) != 2 or\
                (not isinstance(self.__position[0], int)) or\
                (not isinstance(self.__position[1], int)) or\
                self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()

            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")

                for j in range(self.size):
                    print("#", end="")
                print()
