__author__ = 'Ana'

msg_not_possible = 'Swap not possible'


def immutable_tuple(value):
    if primitive_or_string(value):
        return True
    if isinstance(value, tuple):
        for t in value:
            imm = immutable_tuple(t)
            if not imm:
                return False  # found one mutable value
        return True  # this tuple is immutable
    return False


def primitive_or_string(value):
    if isinstance(value, int) or isinstance(value, long) or isinstance(value, float):
        return True
    if isinstance(value, str):
        return True
    return False


def has_method(value, method_name):
    return hasattr(value.__class__, method_name) and callable(getattr(value.__class__, method_name))


def hashable_object(value):
    return has_method(value, '__hash__') and has_method(value, '__cmp__')


def hashable(value):
    if primitive_or_string(value):
        return True
    if hashable_object(value):
        return True
    if isinstance(value, tuple):
        if immutable_tuple(value):
            return True

    return False


def swap(dictionary):
    if dictionary == {}:
        return {}
    if not isinstance(dictionary, dict):
        return msg_not_possible

    keys = dictionary.keys()
    values = dictionary.values()

    for item in values:
        if not hashable(item):
            return msg_not_possible

    return dict(zip(*(values, keys)))
