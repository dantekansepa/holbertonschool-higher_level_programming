#!/usr/bin/python3
"""
A rectangle with width and height.
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Functions
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            if i == self.__height - 1:
                res += ('#' * self.__width)
            else:
                res += (('#' * self.__width) + '\n')
        return res

    def __repr__(self):
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        print("Bye rectangle...")
