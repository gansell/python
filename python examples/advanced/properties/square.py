"""Properties with decorators.
"""


class Square(object):
    """A square using properties with decorators.
    """

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        """Calculate the area of the square when the
        attribute is accessed."""
        return self.side * self.side

    @area.setter
    def area(self, value):
        """Don't allow setting."""
        print "Can't set the area"

    @area.deleter
    def area(self):
        """Don't allow deleting."""
        print "Can't delete the area."


if __name__ == '__main__':

    square = Square(5)
    print 'area:', square.area
    print 'try to set'
    square.area = 10
    print 'area:', square.area
    print 'try to delete'
    del square.area
    print 'area:', square.area
