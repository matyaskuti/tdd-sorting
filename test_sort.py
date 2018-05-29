import unittest

from sort import sort


class TestSort(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertListEqual(sort([]), [])

    def test_sort_list_with_one_element(self):
        self.assertListEqual(sort([42]), [42])


if __name__ == '__main__':
    unittest.main()
