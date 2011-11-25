


class Square(object):
    def __init__(self, side):
        self.side = side
    def aget(self):
        return self.side * self.side
    def aset(self, value):
        print "Can't set the area"
    def adel(self):
        print "Can't delete the area."
    area = property(aget, aset, adel, doc='Area of the square')

s = Square(5)
print s.area
print Square.area.__doc__
