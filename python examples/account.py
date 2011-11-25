class InputDescriptor(object):
    """A simple descriptor"""
    def __init__(self):
        self.__value = 0
        a = 1
        b = 2
    def __set__(self, instance, value):
        print 'setting value is', value
        if value > 0:
            self.__value = value;
        else:
            print 'invalid value'
    def __get__(self, instance, cls):
        print 'getting value', self.__value
        return self.__value
    def __delete__(self, instance):
        print 'Cannot delete'


class Account(object):    
    attr = InputDescriptor()


class Price(object):
    def __init__(self):
        self.__value = 0
        x = 1
        y = 2
        z = 3
        print x, y, z
    @property
    def total(self):
        return self.__value * 1.20
        print 'hello'
    @total.setter
    def total(self, value):
        self.__value = value
    @total.deleter
    def total(self):
        print 'cannot delete total'


if __name__ == '__main__':

    a = Account()
    print a.attr
    a.attr = 100
    print a.attr
    a.attr = -12


    p = Price()
    p.total = 9.99
    print round(p.total, 2)
    
    



    










