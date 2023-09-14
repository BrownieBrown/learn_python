from unittest import TestCase

from algorithms.searching.binary_search.challenges.find_first_occurrence import find_first_occurrence


class TestFindFirstOccurrence(TestCase):
    def test_standard_case(self):
        arr = [1, 2, 3, 3, 3, 4, 5]
        target = 3
        self.assertEqual(find_first_occurrence(arr, target), 2)

    def test_no_occurrence(self):
        arr = [1, 2, 4, 5, 6]
        target = 3
        self.assertEqual(find_first_occurrence(arr, target), -1)

    def test_occurrence_at_end(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        self.assertEqual(find_first_occurrence(arr, target), 9)

    def test_occurrence_at_start(self):
        arr = [1, 1, 2, 3, 4, 5]
        target = 1
        self.assertEqual(find_first_occurrence(arr, target), 0)

    def test_single_element_matching(self):
        arr = [3]
        target = 3
        self.assertEqual(find_first_occurrence(arr, target), 0)

    def test_single_element_not_matching(self):
        arr = [3]
        target = 5
        self.assertEqual(find_first_occurrence(arr, target), -1)

    def test_empty_array(self):
        arr = []
        target = 5
        self.assertEqual(find_first_occurrence(arr, target), -1)
