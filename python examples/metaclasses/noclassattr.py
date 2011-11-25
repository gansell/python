"""Preventing non-callable class attributes with a metaclass
"""

class NoClassAttributes(type):
    """No non-callable class attributes allowed
    """
    def __init__(self, name, bases, dict):
        allowed = set(['__module__', '__metaclass__', '__doc__'])
        for key, value in dict.items():
            if ((key not in allowed) and 
            (not hasattr(value, '__call__'))):
                msg = 'Found non-callable class attribute "%s". ' % key
                msg += 'Only methods are allowed.'
                raise Exception(msg)
        super(NoClassAttributes, self).__init__(name, bases, dict)


if __name__ == '__main__':

    class AttributeLess:
        """Only methods works_
        """
        __metaclass__ = NoClassAttributes
        def meth(self):
            """This is allowed'
            """
            print 'Hello from AttributeLess.'

    attributeless = AttributeLess()
    attributeless.meth()
    

    class WithAttribute:
        """Has non-callable class attribute.
        Will raise an exception.
        """
        __metaclass__ = NoClassAttributes
        a = 10
        def meth(self):
            """This is allowed'
            """
            print 'Hello from WithAttribute'

