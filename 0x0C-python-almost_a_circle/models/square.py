#!/usr/bin/python3
'''Square module'''
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        return self.height
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.height = self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif len(kwargs) != 0:
            if 'size' in kwargs:
                self.width = self.height = kwargs['size']
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        square_dict = {}
        if self.id != None:
            square_dict['id'] = self.id
        if self.x !=None:
            square_dict['x'] = self.x
        if self.height !=None:
            square_dict['size'] = self.height
        if self.y !=None:
            square_dict['y'] = self.y
        return square_dict
            
