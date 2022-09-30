#!/usr/bin/python3

"""Comments"""


class Square():

    """Square"""

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_mySquare(self):
        """Perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String"""
        return "{}/{}".format(self.height, self.width)


if __name__ == "__main__":

    s = Square()
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_mySquare())
