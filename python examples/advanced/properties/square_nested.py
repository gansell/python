"""Use a decorator to allow nested properties.
"""


def nested_property(func):
    """Make defining properties simpler
    """
    return property(**func())


class Square(object):
    """A square using properties with decorators.
    """

    def __init__(self, side):
        self.side = side

    @nested_property
    def area():
        """Property that defines is methods nested.
        """

        def fget(self):
            """
            Calculate the area of the square
            when the attribute is accessed.
            """
            return self.side * self.side

        def fset(self, value):
            """Don't allow setting."""
            print "Can't set the area"

        def fdel(self):
            """Don't allow deleting."""
            print "Can't delete the area."

        return locals()


if __name__ == '__main__':

    square = Square(5)
    print 'area:', square.area
    print 'try to set'
    square.area = 10
    print 'area:', square.area
    print 'try to delete'
    del square.area
    print 'area:', square.area
