class MyMetaClass(type):
    """MyMetaClass will prevent class names with
    more than 30 chars"""
    def __init__(self, name, bases, dict):
        allowed = set(['__module__', '__metaclass__', '__doc__'])
        for key, value in dict.items():
            if name not in allowed:
                if (hasattr(value, '__call__')):
                    name_len = len(key)
                    if name_len > 30:

                        raise Exception('Too Long')
        super(MyMetaClass, self).__init__(name, bases, dict)

class MyClass:
    """Test Class"""
    __metaclass__ = MyMetaClass
    def __init__(self):
        print 'init myclass'
    def im_ok(self):
        print 'good'
    def asdfghjklpoiuytrewqzxcvbnmlkjhfdds(self):
        print 'bad'


if __name__ == '__main__':
    m = MyClass()




    
                    