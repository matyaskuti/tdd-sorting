import unittest

from sort import sort


class TestSort(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertListEqual(sort([]), [])


if __name__ == '__main__':
    unittest.main()
