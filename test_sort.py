import unittest

from sort import sort


class TestSort(unittest.TestCase):
    def test_sort_empty_list(self):
        self._assert_list_sorted([], [])

    def test_sort_list_with_one_element(self):
        self._assert_list_sorted([42], [42])

    def _assert_list_sorted(self, list1, list2):
        self.assertListEqual(sort(list1), list2)


if __name__ == '__main__':
    unittest.main()
