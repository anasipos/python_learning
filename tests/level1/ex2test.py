__author__ = 'anamaria.sipos'

from exercises.level1 import ex2
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

# numeric and string

    def test_merge_numeric_return_sum(self):
        num1, num2 = 20, 33.5
        result = ex2.merge(num1, num2)
        self.assertEqual(53.5, result)

    def test_merge_strings(self):
        str1, str2 = 'mama_are', '_mere'
        result = ex2.merge(str1, str2)
        self.assertEqual('mama_are_mere', result)

# lists

    def test_merge_empty_lists_return_empty_list(self):
        list1, list2 = [], []
        result = ex2.merge(list1, list2)
        self.assertTrue(type(result) is list)
        self.assertEqual([], result)

    def test_merge_list_with_empty_lists_return_first_list(self):
        list1, list2 = [1, 2, 3], []
        result = ex2.merge(list1, list2)
        self.assertTrue(type(result) is list)
        self.assertEqual(list1, result)

    def test_lists_return_list(self):
        list1 = [1, 2, 3]
        list2 = [[4, 5], [6, 7]]
        result = ex2.merge(list1, list2)
        self.assertTrue(type(result) is list)
        self.assertEqual([1, 2, 3, [4, 5], [6, 7]], result)

# sets

    def test_merge_empty_sets_return_empty_set(self):
        set11, set2 = set(), set()
        result = ex2.merge(set11, set2)
        self.assertTrue(type(result) is set)
        self.assertEqual(set(), result)

    def test_merge_set_with_empty_sets_return_first_set(self):
        set1, set2 = {1, 2, 3}, set()
        result = ex2.merge(set1, set2)
        self.assertTrue(type(result) is set)
        self.assertEqual(set1, result)

    def test_merge_sets_return_set(self):
        set1 = {1, 2, 3, 4, 'a', 'b'}
        set2 = {'a', 'b', 'c', 1, 2, 3, 4, 5, 6}
        result = ex2.merge(set1, set2)
        self.assertTrue(type(result) is set)
        self.assertTrue(result == {1, 2, 3, 4, 5, 6, 'a', 'b', 'c'})

# maps

    def test_merge_empty_maps_return_empty_map(self):
        map1, map2 = {}, {}
        result = ex2.merge(map1, map2)
        self.assertTrue(type(result) is dict)
        self.assertEqual({}, result)

    def test_merge_map_with_empty_maps_return_first_map(self):
        map1, map2 = {'a': 'ana', 'm': 'mama'}, {}
        result = ex2.merge(map1, map2)
        self.assertTrue(type(result) is dict)
        self.assertEqual(map1, result)

    def test_merge_maps_different_keys_return_map(self):
        map1, map2 = {'a': 'ana', 'm': 'mama'}, {'x': 1, 'y': 2}
        result = ex2.merge(map1, map2)
        self.assertTrue(type(result) is dict)
        self.assertEqual({'a': 'ana', 'm': 'mama', 'x': 1, 'y': 2}, result)

    def test_merge_maps_same_keys_return_merged_map(self):
        map1, map2 = {'a': 'ana', 'm': 'mama'}, {'x': 1, 'y': 2, 'a': 'are'}
        result = ex2.merge(map1, map2)
        self.assertTrue(type(result) is dict)
        self.assertEqual({'a': 'anaare', 'm': 'mama', 'x': 1, 'y': 2}, result)

    def test_merge_maps_same_keys_return_merged_map_2(self):
        a = {'x': [1, 2, 3], 'y': 1, 'z': {1, 2, 3}, 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
        b = {'x': [4, 5, 6], 'y': 4, 'z': {4, 2, 3}, 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
        result = ex2.merge(a, b)
        expected_result = {'x': [1, 2, 3, 4, 5, 6], 'y': 5, 'z': {1, 2, 3, 4}, 'w': 'qweqweasdf',
                           't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer")}
        self.assertEqual(expected_result, result)

# different types

    def test_merge_set_and_list_return_tuple(self):
        set1 = {1, 2, 3}
        list1 = ['a', 'b', 'c']
        result = ex2.merge(set1, list1)
        self.assertTrue(type(result) is tuple)
        self.assertEqual(result, (set1, list1))


# if __name__ == '__main__':
# unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
