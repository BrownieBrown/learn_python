from unittest import TestCase

from algorithms.searching.binary_search.challenges.find_boundary import find_boundary


class TestBoundaryFunction(TestCase):
    def test_all_false(self):
        arr = [False, False, False, False]
        self.assertEqual(find_boundary(arr), -1)  # No boundary because all elements are False

    def test_all_true(self):
        arr = [True, True, True, True]
        self.assertEqual(find_boundary(arr), 0)  # Boundary at the first element because all elements are True

    def test_mixed_values(self):
        arr = [False, False, True, True]
        self.assertEqual(find_boundary(arr), 2)  # Boundary where False changes to True

    def test_single_value_false(self):
        arr = [False]
        self.assertEqual(find_boundary(arr), -1)  # No boundary because there's only one False element

    def test_single_value_true(self):
        arr = [True]
        self.assertEqual(find_boundary(arr), 0)  # Boundary at the first (and only) element

    def test_large_mixed_values(self):
        arr = [False] * 10000 + [True] * 10000
        self.assertEqual(find_boundary(arr), 10000)  # Boundary where False changes to True in a large list
