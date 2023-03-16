import unittest
from train import *
from feature_importance import *


class TestFindLargestSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_largest_sum([1, 2, 3, 4]), 7)
        self.assertEqual(find_largest_sum([4, 2, 3, 1]), 7)

    def test_negative_numbers(self):
        self.assertEqual(find_largest_sum([-1, -2, -3, -4]), -1)
        self.assertEqual(find_largest_sum([-4, -2, -3, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(find_largest_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(find_largest_sum([5, -4, 6, -7, 8]), 9)

    def test_empty_list(self):
        self.assertEqual(find_largest_sum([]), 0)

    def test_single_item_list(self):
        self.assertEqual(find_largest_sum([5]), 5)


if __name__ == '__main__':
    unittest.main()