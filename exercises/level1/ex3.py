__author__ = 'anamaria.sipos'


def get_value_of_smallest_key(dictionary):
    smallest_key = None
    for key in dictionary.keys():
        if (smallest_key is None) or (key < smallest_key):
            smallest_key = key

    return dictionary[smallest_key]


def is_smaller(dict1, dict2):
    dict1_smaller = False

    if (type(dict1) is dict) and (type(dict2) is dict):
        value1 = get_value_of_smallest_key(dict1)
        value2 = get_value_of_smallest_key(dict2)
        if value1 < value2:
            dict1_smaller = True

    return dict1_smaller


def apply_selection_sort(dict_list):

    for i in range(0, len(dict_list) - 1):
        index = i
        for j in range(i + 1, len(dict_list)):
            if is_smaller(dict_list[j], dict_list[index]):
                index = j

        smaller_dict = dict_list[index]
        dict_list[index] = dict_list[i]
        dict_list[i] = smaller_dict
        # dict on position index has now position i

    return dict_list


def get_sort_order(original, sorted):
    sort_order = []
    for i in range(0, len(original)):
        sort_order.append(sorted.index(original[i]))
    return sort_order


def sort_dictionaries(dict_list):
    if len(dict_list) == 0:
        return []
    if len(dict_list) == 1:
        return [0]

    maps = dict_list[:]
    sorted_maps = apply_selection_sort(maps)
    return get_sort_order(dict_list, sorted_maps)


def extract_key_value(the_line):
    res = the_line.split(' ')
    key = res[0].strip('\'').strip('\"')
    value = int(res[1])
    return key, value


def read_from_file(file_path):
    dict_list = []
    dictionary = {}

    try:
        with open(file_path) as f:
            for line in f:
                the_line = line.strip()
                if the_line != '':
                    key, value = extract_key_value(the_line)
                    dictionary[key] = value
                else:
                    if dictionary != {}:
                        dict_list.append(dictionary)
                        dictionary = {}

            if dictionary != {}:
                dict_list.append(dictionary)
    except IOError:
        pass
    return dict_list


def write_to_file(file_path, dictionaries_position):
    f = None
    try:
        f = open(file_path, 'w')
        for pos in dictionaries_position:
            f.write(str(pos) + '\n')
    except IOError:
        pass
    finally:
        if f is not None:
            f.close()


def sort_dictionaries_in_file(input_file_path, output_file_path):
    '''
    Writes the sort order of the dictionaries read from the input file to the output file.
    :param input_file_path: the input file where the dictionaries are
    :param output_file_path: the output file path where to put the resulting sort order
    :return: does not return anything
    '''

    dictionaries = read_from_file(input_file_path)
    write_to_file(output_file_path, sort_dictionaries(dictionaries))
