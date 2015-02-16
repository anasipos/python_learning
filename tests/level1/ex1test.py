__author__ = 'anamaria.sipos'

from exercises.level1 import ex1
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_flatten_empty_lists_return_empty(self):
        list1, list2 = [], []
        (l1, l2) = ex1.flatten(list1, list2, 10)
        self.assertEqual([], l1)
        self.assertEqual([], l2)

    def test_flatten_one_level_list_return_same(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        (l1, l2) = ex1.flatten(list1, list2, 10)
        self.assertEqual(list1, l1)
        self.assertEqual(list2, l2)

    def test_flatten_max_level_0_return_same(self):
        list1 = [[1, 2], [3, 4]]
        list2 = [['a', 'b'], ['c', 'd']]
        (l1, l2) = ex1.flatten(list1, list2, 0)
        self.assertEqual(list1, l1)
        self.assertEqual(list2, l2)

    def test_flatten_two_level_list_max_depth_unlimited_return_flattened(self):
        list1 = [[1, 2], [3, 4]]
        list2 = [['a', 'b'], ['c', 'd']]
        (l1, l2) = ex1.flatten(list1, list2, 99)
        self.assertEqual([1, 2, 3, 4], l1)
        self.assertEqual(['a', 'b', 'c', 'd'], l2)

    def test_flatten_two_level_list_max_depth_1_return_flattened(self):
        list1 = [[1, 2], [3, 4]]
        list2 = [['a', 'b'], ['c', 'd']]
        (l1, l2) = ex1.flatten(list1, list2, 1)
        self.assertEqual([1, 2, 3, 4], l1)
        self.assertEqual(['a', 'b', 'c', 'd'], l2)

    def test_flatten_four_level_list_max_depth_unlimited_return_flattened(self):
        list1 = [[1, [2, 3], [4, [5, 6]]], [[7], 8, [], [[9]]]]
        list2 = []
        (l1, l2) = ex1.flatten(list1, list2, 99)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], l1)
        self.assertEqual([], l2)

    def test_flatten_three_level_list_max_depth_1_return_2_level(self):
        list1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        list2 = [['a', 'b'], ['c', 'd']]
        (l1, l2) = ex1.flatten(list1, list2, 1)
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8]], l1)
        self.assertEqual(['a', 'b', 'c', 'd'], l2)


# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
