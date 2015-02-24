__author__ = 'anamaria.sipos'

instances = dict()


class SingletonFactory(type):
    # called when instances of the required class are created
    def __call__(cls, *args, **kwds):
        if cls not in instances:
            instances[cls] = type.__call__(cls, *args, **kwds)
        return instances[cls]

    # called when the class is created
    def __new__(mcs, name, bases, attrs):
        return type.__new__(mcs, name, bases, attrs)
