import random
import unittest

from sort import bubble_sort, quick_sort


class TestBubbleSort(unittest.TestCase):
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

    def test_sort_three_elements_list_last_two_out_of_order(self):
        self._assert_list_sorted([1, 42, 23], [1, 23, 42])

    def test_sort_three_elements_list_first_is_last(self):
        self._assert_list_sorted([23, 42, 1], [1, 23, 42])

    def test_sort_three_elements_list_reversed(self):
        self._assert_list_sorted([42, 23, 1], [1, 23, 42])

    def test_sort_three_elements_list_with_duplicate(self):
        self._assert_list_sorted([42, 42, 1], [1, 42, 42])

    def test_sort_list_reversed_with_duplications(self):
        self._assert_list_sorted(
            [42, 42, 23, 23, 1, 1], [1, 1, 23, 23, 42, 42]
        )

    def test_sort_large_list(self):
        unsorted_list = random.sample(range(100000), 1000)
        sorted_list = self._sort_list(unsorted_list)

        self.assertEqual(len(unsorted_list), len(sorted_list))
        self._assert_list_is_sorted(sorted_list)

    def _assert_list_is_sorted(self, sorted_list):
        for i in range(len(sorted_list)-1):
            self.assertTrue(sorted_list[i] <= sorted_list[i+1])

    def _assert_list_sorted(self, list1, list2):
        self.assertListEqual(self._sort_list(list1), list2)

    @staticmethod
    def _sort_list(list_):
        return bubble_sort(list_)


class TestQuickSort(TestBubbleSort):
    @staticmethod
    def _sort_list(list_):
        return quick_sort(list_)


if __name__ == '__main__':
    unittest.main()
