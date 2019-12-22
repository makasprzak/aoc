from unittest import TestCase
from day_7.sequence_combinator import get_combinations


class TestGet_combinations(TestCase):
    def test_get_combinations_1(self):
        combinations = get_combinations({0})
        self.assertEqual(1, len(combinations))
        self.assertSequenceEqual([0], combinations[0])

    def test_get_combinations_2(self):
        combinations = get_combinations({0, 1})
        self.assertEqual(2, len(combinations))
        self.assertIn([0 ,1], combinations)
        self.assertIn([1 ,0], combinations)

    def test_get_combinations_3(self):
        combinations = get_combinations({0, 1, 2})
        self.assertEqual(6, len(combinations))
        self.assertIn([0, 1, 2], combinations)
        self.assertIn([0, 2, 1], combinations)
        self.assertIn([1, 0, 2], combinations)
        self.assertIn([1, 2, 0], combinations)
        self.assertIn([2, 0, 1], combinations)
        self.assertIn([2, 1, 0], combinations)

    def test_get_combinations_5(self):
        combinations = get_combinations({0, 1, 2, 3, 4})
        self.assertEqual(1*2*3*4*5, len(combinations))
