"""A typical data descriptor.
"""


class DataDescriptor(object):
    """A simple descriptor.
    """
    def __init__(self):
        self.value = 0
    def __get__(self, instance, cls):
        print 'data descriptor __get__'
        return self.value
    def __set__(self, instance, value):
        print 'data descriptor __set__'
        try:
            self.value = value.upper()
        except AttributeError:
            self.value = value
    def __delete__(self, instance):
        print "Don't like to be deleted." 
