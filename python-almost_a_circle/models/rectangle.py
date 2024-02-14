#!/usr/bin/python3
''' Rectangle Module Doc '''


from models.base import Base


class Rectangle(Base):
    ''' Rectangle Class Doc '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value, True)
        self.__y = value

    def validator(self ,name, value, zero_value = False):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not zero_value and  value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if zero_value and value < 0:
            raise ValueError("{} must be >= 0".format(name))


