from unittest import TestCase

from algorithms.searching.binary_search.challenges.find_min_rotated import find_min_rotated


class TestFindMinRotated(TestCase):
    def test_standard_cases(self):
        self.assertEqual(find_min_rotated([4, 5, 6, 7, 0, 1, 2]), 4)
        self.assertEqual(find_min_rotated([3, 4, 5, 1, 2]), 3)
        self.assertEqual(find_min_rotated([5, 1, 2, 3, 4]), 1)

    def test_edge_cases(self):
        self.assertEqual(find_min_rotated([1, 2, 3, 4, 5]), 0)  # Not rotated
        self.assertEqual(find_min_rotated([2, 1]), 1)
        self.assertEqual(find_min_rotated([1]), 0)  # single element
