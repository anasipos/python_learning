__author__ = 'anamaria.sipos'

from itertools import combinations
from itertools import chain
from itertools import imap


class SubsetArgError(Exception):
    pass


def subsets(input_set):
    if type(input_set) is not set:
        raise SubsetArgError
    return imap(set, chain.from_iterable(combinations(input_set, r) for r in reversed(range(len(input_set) + 1))))
