#!/usr/bin/python3

"""Comments"""


class Square():

    """Square"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """init"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=3, height=3)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
