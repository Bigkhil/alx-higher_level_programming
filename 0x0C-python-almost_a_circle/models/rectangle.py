#!/usr/bin/python3
"""class Rectangle"""
from .base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle"""

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area method"""
        return self.__height * self.__width

    def display(self):
        """display method"""
        print("\n" * self.__y, end="")
        print(((" " * self.__x) +
               ("#" * self.__width) + '\n') * self.__height, end="")

    def __str__(self):
        """str method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " + \
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update method"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if len(kwargs) != 0:
                if 'width' in kwargs:
                    self.__width = kwargs['width']
                if 'height' in kwargs:
                    self.__height = kwargs['height']
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'x' in kwargs:
                    self.__x = kwargs['x']
                if 'y' in kwargs:
                    self.__y = kwargs['y']

    def to_dictionary(self):
        """to_dictionary method"""
        rect_dict = {}
        if self.x is not None:
            rect_dict['x'] = self.x
        if self.y is not None:
            rect_dict['y'] = self.y
        if self.id is not None:
            rect_dict['id'] = self.id
        if self.height is not None:
            rect_dict['height'] = self.height
        if self.width is not None:
            rect_dict['width'] = self.width
        return rect_dict
