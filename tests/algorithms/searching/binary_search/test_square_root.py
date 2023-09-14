from unittest import TestCase

from algorithms.searching.binary_search.challenges.square_root import square_root


class TestSquareRoot(TestCase):
    def test_standard_cases(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(8), 2)  # since the square root of 8 is between 2 and 3, we return 2.
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(100), 10)
        self.assertEqual(square_root(99), 9)  # 9*9=81 < 99 < 10*10=100

    def test_edge_cases(self):
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(2), 1)

    def test_large_numbers(self):
        self.assertEqual(square_root(10000000000), 100000)
        self.assertEqual(square_root(9999999999), 99999)
