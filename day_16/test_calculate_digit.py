from unittest import TestCase
from day_16.fft import calculate_digit, decode
from day_16.fft2 import create_digit_calculator
import numpy as np


class TestFft(TestCase):
    def test_calculate_digit(self):
        self.assertEqual(2, calculate_digit(dict(), 0, [1, 2, 3]))
        self.assertEqual(0, calculate_digit(dict(), 0, [1, 1, 1, 1]))
        self.assertEqual(1, calculate_digit(dict(), 0, [2, 1, 1, 1]))
        self.assertEqual(1, calculate_digit(dict(), 0, [1, 1, 2, 1]))
        self.assertEqual(1, calculate_digit(dict(), 0, [1, 9, 2, 1]))
        self.assertEqual(3, calculate_digit(dict(), 0, [5, 9, 2, 1]))
        self.assertEqual(3, calculate_digit(dict(), 0, [5, 9, 2, 1]))
        self.assertEqual(3, calculate_digit(dict(), 1, [5, 9, 2, 1, 9, 2, 9]))
        self.assertEqual(0, calculate_digit(dict(), 0, [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))
        self.assertEqual(5, calculate_digit(dict(), 0, [1, 2, 4, 4, 1, 2, 4, 4, 1, 2, 4, 4, 1, 2, 4, 4, 1, 2, 4, 4]))
        self.assertEqual(2, calculate_digit(dict(), 0, [1, 2, 3, 4]))
        self.assertEqual(2, calculate_digit(dict(), 0, [1, 2, 3, 4]))
        self.assertEqual(3, calculate_digit(dict(), 0, [1, 2, 4, 4]))
        self.assertEqual(3, calculate_digit(dict(), 0,
                                            [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4,
                                             5]))
        self.assertEqual(0, calculate_digit(dict(), 0, [1, 2, 4, 4, 2, 1, 2, 4, 4, 2, 1, 2, 4, 4, 2, 1, 2, 4, 4, 2]))
        self.assertEqual(0, calculate_digit(dict(), 0, [0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9]))
        self.assertEqual(0, calculate_digit(dict(), 0, [1, 0, 0, 0, 9, 1, 0, 0, 0, 9, 1, 0, 0, 0, 9, 1, 0, 0, 0, 9]))
        self.assertEqual(0, calculate_digit(dict(), 0, [1, 1, 3, 4, 3, 3, 1, 1, 3, 4, 3, 3]))
        self.assertEqual(0, calculate_digit(dict(), 0,
                                            [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4,
                                             5, 6, 7]))
        self.assertEqual(4, calculate_digit(dict(), 0, [1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(4, calculate_digit(dict(), 0, [1, 2, 3, 4, 5, 6, 7] * 9))
        self.assertEqual(2, calculate_digit(dict(), 0, [1, 2, 3, 4, 6, 2, 3, 2, 1, 2, 3, 4, 6, 2, 3, 2]))
        self.assertEqual(1, calculate_digit(dict(), 0, [1, 2, 3, 4, 6, 2, 3, 2]))
        self.assertEqual(0, calculate_digit(dict(), 1, [1, 2, 3, 4, 5, 6, 7, 8, 7] * 8))
        self.assertEqual(7, calculate_digit(dict(), 1, [1, 2, 3, 4, 5, 6, 7, 8, 7, 8]))
        self.assertEqual(0, calculate_digit(dict(), 9, [1, 2, 3, 4, 5, 6, 7, 8, 7, 8] * 4))

    def test_improved(self):
        self.assertEqual(0, create_digit_calculator([1, 1, 1, 1]).calculate_digit(0))
        self.assertEqual(1, create_digit_calculator([1, 1, 0, 1]).calculate_digit(0))
        self.assertEqual(2, create_digit_calculator([1, 1, 0, 1, 1, 2, 1, 1]).calculate_digit(1))
        self.assertEqual(1, create_digit_calculator([1, 1, 0, 1, 1, 2]).calculate_digit(1))
        self.assertEqual(8, create_digit_calculator([3, 1, 0, 5, 6, 2]*3).calculate_digit(1))

    def test_decode(self):
        self.assertEqual([4,3,1], decode([1,1,1,1], 1, 1, 2))
        self.assertEqual([6,3,1], decode([1,1,1,1], 9, 3, 2))
        self.assertEqual([6,1,5,0,6,3,1], decode([1,1,1,1], 5, 3, 2))
