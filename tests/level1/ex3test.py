__author__ = 'anamaria.sipos'

from exercises.level1 import ex3
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_sort_dictionaries_empty_list_return_empty_sort_order(self):
        dictionaries = []
        result = ex3.sort_dictionaries(dictionaries)
        self.assertEqual([], result)

    def test_sort_dictionaries_one_dictionary_return_list_with_0(self):
        dictionaries = [{'a': 'ana'}]
        result = ex3.sort_dictionaries(dictionaries)
        self.assertEqual([0], result)

    def test_sort_dictionaries_two_equal_dictionaries_return_same_order(self):
        dictionaries = [{'a': 'ana', 'b': 'baba'}, {'a': 'ana', 'b': 'baba'}]
        result = ex3.sort_dictionaries(dictionaries)
        self.assertEqual([0, 0], result)

    def test_sort_dictionaries(self):
        dictionaries = [{'aa': 1, 'bb': 2}, {'ab': 0, 'ba': 1}, {'ac': 2, 'ba': 9}]
        result = ex3.sort_dictionaries(dictionaries)
        self.assertEqual([1, 0, 2], result)

    def test_read_from_inexistent_file_return_empty_list(self):
        file = 'bla'
        dicts = ex3.read_from_file(file)
        self.assertEqual([], dicts)

    def test_read_from_file_empty_file_empty_list(self):
        empty_file = 'empty_file.txt'
        dicts = ex3.read_from_file(empty_file)
        self.assertEqual([], dicts)

    def test_read_from_file_return_dictionaries_list(self):
        the_file = 'dicts.txt'
        dicts = ex3.read_from_file(the_file)
        self.assertEqual([{'a': 1, 'b': 2, 'c': 4}, {'b': 40, 'c': 3}, {'a': 56, 'b': -1}], dicts)

    def test_sort_dictionaries_in_file_valid_input_valid_output(self):
        input_file = 'dicts.txt'
        output_file = 'dicts_out.txt'
        ex3.sort_dictionaries_in_file(input_file, output_file)
        self.assertTrue(True)



# if __name__ == '__main__':
# unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
