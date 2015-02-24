import pytest

__author__ = 'anamaria.sipos'
from exercises.level3.ex1 import preorder
from exercises.level3.ex1 import PreorderArgError


def test_empty_tree_raises_error():
    tree = ()
    iterator = preorder(tree)

    with pytest.raises(StopIteration):
        next(iterator)


def test_no_tuple_raise_error():
    tree = [1, 2, 3]
    iterator = preorder(tree)

    with pytest.raises(PreorderArgError):
        next(iterator)


def test_invalid_tree_too_few_nodes_raise_error():
    tree = ('root', None)
    iterator = preorder(tree)

    with pytest.raises(PreorderArgError):
        next(iterator)


def test_invalid_tree_too_many_nodes_raise_error():
    tree = ('a', ('b', None, None), ('c', None, None), ('d', None, None))

    with pytest.raises(PreorderArgError):
        list(preorder(tree))


def test_one_node_tree_iterator_has_one_elem():
    tree = ('a', None, None)
    iterator = preorder(tree)

    elem = next(iterator)
    assert elem == 'a'

    with pytest.raises(StopIteration):
        next(iterator)


def test_three_node_tree_iterator_has_three_elem():
    tree = ('a', ('b', None, None), ('c', None, None))

    expected_order = ['a', 'b', 'c']

    preorder_nodes = list(preorder(tree))

    assert expected_order == preorder_nodes


def test_preorder_traversal():
    tree = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))

    expected_order = ['b', 'a', 'z', 'c', 'zz']

    preorder_nodes = list(preorder(tree))

    assert expected_order == preorder_nodes
