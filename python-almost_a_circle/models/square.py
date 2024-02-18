#!/usr/bin/python3
''' Square Module Doc'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square Class that inherits from Rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update method assigns an argument to each attribute'''
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            attributes = ["id", "size", "x", "y"]

            for attribute in attributes:
                if attribute in kwargs:
                    try:
                        setattr(self, attribute, kwargs[attribute])
                    except Exception:
                        pass

    def to_dictionary(self):
        ''' returns the dictionary representation of a Square'''
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
