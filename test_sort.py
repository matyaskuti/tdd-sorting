import unittest

from sort import sort


class TestSort(unittest.TestCase):
    def test_sort_empty_list(self):
        self._assert_list_sorted([], [])

    def test_sort_list_with_one_element(self):
        self._assert_list_sorted([42], [42])

    def test_sort_list_with_two_elements_in_order(self):
        self._assert_list_sorted([23, 42], [23, 42])

    def test_sort_list_with_two_elements_out_of_order(self):
        self._assert_list_sorted([42, 23], [23, 42])

    def test_sort_three_elements_list_in_order(self):
        self._assert_list_sorted([1, 23, 42], [1, 23, 42])

    def test_sort_three_elements_list_first_two_out_of_order(self):
        self._assert_list_sorted([23, 1, 42], [1, 23, 42])

    def _assert_list_sorted(self, list1, list2):
        self.assertListEqual(sort(list1), list2)


if __name__ == '__main__':
    unittest.main()
