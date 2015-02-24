__author__ = 'anamaria.sipos'

from exercises.level3.ex3 import SingletonFactory


def test_singleton_class():
    class SingletonClass(object):
        __metaclass__ = SingletonFactory

    instance1 = SingletonClass()
    instance2 = SingletonClass()

    assert instance1 is instance2


def test_singleton_class_with_params():
    class SingletonClassWithParams(object):
        __metaclass__ = SingletonFactory

        def __init__(self, name, age):
            self.name = name
            self.age = age

    instance1 = SingletonClassWithParams('Ana', 99)
    instance2 = SingletonClassWithParams('Maria', 98)

    assert instance1.name == instance2.name
    assert instance1.age == instance2.age

    assert instance1 is instance2


def test_singleton_class_inheritance():
    class SingletonClassWithParams(object):
        __metaclass__ = SingletonFactory

        def __init__(self, name, age):
            self.name = name
            self.age = age

    class SubClass(SingletonClassWithParams):
        def __init__(self, name, age):
            super(SubClass, self).__init__(name, age)

    instance1 = SubClass('Ana', 99)
    instance2 = SubClass('Oana', 87)

    assert instance1.name == instance2.name
    assert instance1.age == instance2.age

    assert instance1 is instance2