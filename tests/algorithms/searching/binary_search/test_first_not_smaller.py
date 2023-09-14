from unittest import TestCase

from algorithms.searching.binary_search.challenges.first_not_smaller import first_not_smaller


class TestFirstNotSmaller(TestCase):
    def test_normal_case(self):
        arr = [1, 2, 4, 6, 8, 10]
        target = 5
        self.assertEqual(first_not_smaller(arr, target), 3)

    def test_target_smaller_than_all_elements(self):
        arr = [5, 6, 7, 8, 9]
        target = 3
        self.assertEqual(first_not_smaller(arr, target), 0)

    def test_target_larger_than_all_elements(self):
        arr = [1, 2, 3, 4, 5]
        target = 10
        self.assertEqual(first_not_smaller(arr, target), -1)

    def test_target_equal_to_some_elements(self):
        arr = [1, 2, 4, 4, 4, 6, 7]
        target = 4
        self.assertEqual(first_not_smaller(arr, target), 2)

    def test_empty_array(self):
        arr = []
        target = 3
        self.assertEqual(first_not_smaller(arr, target), -1)

    def test_array_of_same_elements(self):
        arr = [5, 5, 5, 5]
        target = 5
        self.assertEqual(first_not_smaller(arr, target), 0)
