"""Use of descriptor and metaclass to get slots with
given types.
"""


class TypDescriptor(object):
    """Descriptor with type.
    """

    def __init__(self, data_type, default_value=None):
        self.name = None
        self.data_type = data_type
        if default_value:
            self.default_value = default_value
        else:
            self.default_value = data_type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default_value)

    def __set__(self, instance, value):
        if not isinstance(value, self.data_type):
            raise TypeError('Required data type is %s' % self.data_type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError('Cannot delete %r' % instance)


class TypeProtected(type):
    """Metaclass to save descriptor values in slots.
    """

    def __new__(mcl, name, bases, cdict):
        slots = []
        for key, value in cdict.items():
            if isinstance(value, TypDescriptor):
                value.name = '_' + key
                slots.append(value.name)
        cdict['__slots__'] = slots
        return super(TypeProtected, mcl).__new__(mcl, name, bases, cdict)


class MyClass:
    """Test class."""
    __metaclass__ = TypeProtected
    attr1 = TypDescriptor(int)
    attr2 = TypDescriptor(float, 5.5)


if __name__ == '__main__':

    def main():
        """Test it.
        """
        my_inst = MyClass()
        print my_inst.attr1
        print my_inst.attr2
        my_inst.attr1 = 100
        print my_inst.attr1
        # this will fail
        my_inst.unknown = 100

    main()
