__author__ = 'anamaria.sipos'

from exercises.level3.ex2 import subsets
from exercises.level3.ex2 import SubsetArgError
import pytest


def test_invalid_input_raise_error():
    with pytest.raises(SubsetArgError):
        it = subsets([1, 2, 3])
        next(it)


def test_empty_set_one_empty_subset():
    input_set = set()
    iterator = subsets(input_set)

    assert set() == next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


def test_one_elem_set_two_subsets():
    input_set = {'a'}
    iterator = subsets(input_set)

    assert input_set == next(iterator)
    assert set() == next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


def test_two_elements_set_four_subsets():
    input_set = {'a', 'b'}

    output_set = subsets(input_set)

    assert {'a', 'b'} == next(output_set)
    assert {'a'} == next(output_set)
    assert {'b'} == next(output_set)
    assert set() == next(output_set)


def test_three_elements_all_subsets():
    input_set = {'a', 'b', 'c'}

    output_set = subsets(input_set)

    assert {'a', 'b', 'c'} == next(output_set)
    assert {'a', 'c'} == next(output_set)
    assert {'a', 'b'} == next(output_set)
    assert {'b', 'c'} == next(output_set)
    assert {'a'} == next(output_set)
    assert {'c'} == next(output_set)
    assert {'b'} == next(output_set)
    assert set() == next(output_set)




