import unittest

from sort import sort


class TestSort(unittest.TestCase):
    def test_sort_does_nothing(self):
        self.assertIsNone(sort())


if __name__ == '__main__':
    unittest.main()
