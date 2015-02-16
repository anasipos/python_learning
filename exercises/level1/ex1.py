__author__ = 'anamaria.sipos'


def flatten(list_a, list_b, max_depth):
    '''
    Flattens two lists to a given depth
    :param list_a: first list
    :param list_b: second list
    :param max_depth: the max depth for flattening
    :return: the flattened lists
    '''
    return flatten_list(list_a, max_depth), flatten_list(list_b, max_depth)


def flatten_list(l, max_depth):
    if l == [] or max_depth == 0:
        return l

    return flatten_internal(l, 0, max_depth)


def is_type_primitive(the_type):
    return (the_type is int) or (the_type is str) or (the_type is float)


def flatten_internal(l, depth, max_depth):
    result = []

    if depth == max_depth:
        return l

    for i in range(0, len(l)):
        elem = l[i]
        the_type = type(elem)
        if (the_type is list) and len(elem) > 0:
            result.extend(flatten_internal(elem, depth + 1, max_depth))
        elif is_type_primitive(the_type):
            result.append(elem)

    return result

