__author__ = 'anamaria.sipos'


def merge_lists(list1, list2):
    result = []
    if len(list1) == 0:
        result = list2
    elif len(list2) == 0:
        result = list1
    elif len(list1) > 0 and len(list2) > 0:
        result = list1[:]
        result.extend(list2)

    return result


def merge_sets(set1, set2):
    result = set()
    if len(set1) == 0:
        result = set2
    elif len(set2) == 0:
        result = set1
    elif len(set1) > 0 and len(set2) > 0:
        result = set1 | set2

    return result


def merge_maps(dict1, dict2):
    result = {}
    if len(dict1) == 0:
        result = dict2
    elif len(dict2) == 0:
        result = dict1
    elif len(dict1) > 0 and len(dict2) > 0:
        result = dict(dict1)
        for key in dict2.keys():
            if key in result:
                result[key] = merge(result[key], dict2[key])
            else:
                result[key] = dict2[key]

    return result


def merge_same_type(cont1, cont2):
    the_type = type(cont1)

    if the_type is list:
        return merge_lists(cont1, cont2)
    elif the_type is set:
        return merge_sets(cont1, cont2)
    elif the_type is dict:
        return merge_maps(cont1, cont2)
    elif is_numeric(the_type):
        return cont1 + cont2
    elif the_type is str:
        return cont1 + cont2


def is_numeric(the_type):
    return (the_type is int) or (the_type is float) or (the_type is long)


def merge_numeric(num1, num2):
    return num1 + num2


def merge(cont1, cont2):
    type1 = type(cont1)
    type2 = type(cont2)

    if type1 == type2:
        return merge_same_type(cont1, cont2)
    elif is_numeric(type1) and is_numeric(type2):
        return merge_numeric(cont1, cont2)
    return cont1, cont2