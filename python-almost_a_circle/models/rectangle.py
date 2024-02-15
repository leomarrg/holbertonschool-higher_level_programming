#!/usr/bin/python3
"""
Defining a class called Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class that defines a new rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Task 2 and 3 """

    @property
    def width(self):
        """method width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """method width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be a > 0")
        self.__width = value

    @property
    def height(self):
        """method height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """method height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """method x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """method x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """method y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """method y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Task 4"""

    def area(self):
        """Public method that returns area of a rectangle"""
        return self.width * self.height

    """Task 5"""
    """Task 7 is to take into consideration x and y"""

    def display(self):
        """Public method that prints a rectangle #"""
        if self.width == 0 or self.height == 0:
            print("")

        for i in range(self.height):
            if self.y >= 0:
                print(" " * self.y, end='')
            for j in range(self.width):
                if self.x >= 0:
                    print("" * self.x, end='')
                print('#', end='')
            print()

    """Task 6"""
    def __str__(self):
        """__str__ method that return is x/y width/height"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
