class DataDescriptor(object):
    def __init__(self):
        self.default = 0
        self.values = {}
    def __get__(self, instance, cls):
        print '__get__'
        return self.values.get(id(instance), self.default)
    def __set__(self, instance, value):
        print '__set__'
        try:
            value = value.upper()
        except AttributeError:
            pass
        self.values[id(instance)] = value
    def __delete__(self, instance):
        print instance
        print "Don't like to be deleted." 


attr_inst = DataDescriptor()

class Strange(object):
    attr = attr_inst

class Strange2(object):
    attr = attr_inst    


def check():
    strange = Strange()
    print 'attr', strange.attr
    print 'setting attr value to 5'
    strange.attr = 5
    print 'getting attr `value`',  strange.attr
    print 'setting attr `value` to "Hello"'
    strange.attr = 'Hello'
    print 'getting attr `value`'
    strange.attr
    print 'dict:', strange.__dict__
    print 'setting `new` to 100`'
    strange.new = 100
    print 'dict:', strange.__dict__
    print 'dir(strange)', dir(strange)
    print 'Strange.attr', Strange.attr
    print 'strange.attr', strange.attr
    del strange.attr
    strange2 = Strange2()
    del strange.attr


if __name__ == '__main__':
    check()