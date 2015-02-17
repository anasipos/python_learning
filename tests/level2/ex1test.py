__author__ = 'anamaria.sipos'

from exercises.level2 import ex1
import unittest

msg_not_possible = 'Swap not possible'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_swap_empty_return_empty(self):
        the_dict = {}
        result = ex1.swap(the_dict)
        self.assertEqual({}, result)

    def test_swap_not_dictionary_return_swap_not_possible(self):
        result = ex1.swap([1, 2, 3])
        self.assertEqual(msg_not_possible, result)

    def test_swap_values_immutable_numbers_return_swapped_dictionary(self):
        the_map = {'a': 1, 'b': 2L, 'c': 3.3}
        result = ex1.swap(the_map)
        self.assertEqual({1: 'a', 2L: 'b', 3.3: 'c'}, result)

    def test_swap_values_immutable_string_return_swapped_dictionary(self):
        the_map = {'a': 'aa', 'b': 'bb', 'c': 'cc'}
        result = ex1.swap(the_map)
        self.assertEqual({'aa': 'a', 'bb': 'b', 'cc': 'c'}, result)

    def test_swap_values_immutable_tuples_return_swapped_dictionary(self):
        the_map = {'a': (1, 2), 'b': (('a', 'b'), ('c', 'd')), 'c': (((1, 2), (3, 4)), 5)}
        result = ex1.swap(the_map)
        self.assertEqual({(1, 2): 'a', (('a', 'b'), ('c', 'd')): 'b', (((1, 2), (3, 4)), 5): 'c'}, result)

    def test_swap_values_mutable_tuples_return_swap_not_possible(self):
        the_map = {'a': (1, 2), 'b': (('a', [1, 2]), ('c', ['d', 'e'])), 'c': (((1, 2), (3, 4)), 5)}
        result = ex1.swap(the_map)
        self.assertEqual(msg_not_possible, result)

    def test_swap_values_unhashable_object_return_swap_not_possible(self):
        class Unhashable(object):
            pass

        the_map = {'a': Unhashable(), 'b': 2, 'c': 3}
        result = ex1.swap(the_map)
        self.assertEqual(msg_not_possible, result)

    def test_swap_values_hashable_object_return_swapped_dict(self):
        class Hashable(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __hash__(self):
                return self.x + self.y

            def __cmp__(self, other):
                return self.x - other.x

        h1 = Hashable(1, 2)
        h2 = Hashable(3, 4)
        the_map = {'a': h1, 'b': h2, 'c': 1}
        result = ex1.swap(the_map)
        self.assertEqual({h1: 'a', h2: 'b', 1: 'c'}, result)




# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
