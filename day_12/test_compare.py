from unittest import TestCase
from day_12.moon import compare, Moon, Coords, parse_moon, equal


class TestMoons(TestCase):
    def test_compare(self):
        self.assertEqual(1, compare(3, 1))
        self.assertEqual(-1, compare(1, 3))
        self.assertEqual(0, compare(3, 3))

    def test_parse_moon(self):
        self.assertEqual(Coords(1, 2, 3), parse_moon("<x=1, y=2, z=3>").pos)

    def test_equal(self):
        self.assertTrue(equal([Moon(Coords(1,2,3)), Moon(Coords(3,2,1))], [Moon(Coords(1,2,3)), Moon(Coords(3,2,1))]))
        self.assertFalse(equal([Moon(Coords(1,2,3)), Moon(Coords(3,2,1))], [Moon(Coords(1,2,3)), Moon(Coords(3,2,2))]))
