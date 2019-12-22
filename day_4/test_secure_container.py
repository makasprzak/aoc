from unittest import TestCase
from day_4.secure_container import is_within_range, has_adjacent_digits, never_decreases, count


class TestSecureContainer(TestCase):
    def test_is_within_range(self):
        self.assertTrue(is_within_range(200000, "100000-300000"))
        self.assertFalse(is_within_range(400000, "100000-300000"))
        self.assertFalse(is_within_range(1, "100000-300000"))
        self.assertFalse(is_within_range(200000, "300000-300002"))

    def test_has_adjacent_digits(self):
        self.assertTrue(has_adjacent_digits(122345))
        self.assertTrue(has_adjacent_digits(123477))
        self.assertFalse(has_adjacent_digits(123456))
        self.assertFalse(has_adjacent_digits(122256))
        self.assertTrue(has_adjacent_digits(222122))

    def test_never_decreases(self):
        self.assertTrue(never_decreases(123456))
        self.assertFalse(never_decreases(121456))
        self.assertFalse(never_decreases(123450))

    def test_count(self):
        print(count("235741-706948"))

