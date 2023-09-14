from unittest import TestCase

from algorithms.searching.binary_search.binary_search import binary_search


class TestBinarySearch(TestCase):
    def setUp(self):
        self.sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_element_present(self):
        # Test that the function can find an element that is present
        self.assertEqual(binary_search(self.sorted_list, 5), 4)  # 5 is present at index 4

    def test_element_absent(self):
        # Test that the function returns -1 for absent elements
        self.assertEqual(binary_search(self.sorted_list, 11), -1)

    def test_lowest_element(self):
        # Test that the function can find the lowest element
        self.assertEqual(binary_search(self.sorted_list, 1), 0)  # 1 is present at index 0

    def test_highest_element(self):
        # Test that the function can find the highest element
        self.assertEqual(binary_search(self.sorted_list, 10), 9)  # 10 is present at index 9

    def test_empty_list(self):
        # Test that the function returns -1 when given an empty list
        self.assertEqual(binary_search([], 5), -1)
