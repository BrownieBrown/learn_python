from unittest import TestCase

from algorithms.sorting.bubble_sort import sort_list


class TestBubbleSort(TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_list([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(sort_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(sort_list([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(sort_list([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_list([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_negative_numbers(self):
        self.assertEqual(sort_list([4, -2, 2, 8, -3, 3, 1]), [-3, -2, 1, 2, 3, 4, 8])
