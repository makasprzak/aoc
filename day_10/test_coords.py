from unittest import TestCase
from day_10.asteroids import Coords, group_by_angle, index_from_up
from math import pi


class TestCoords(TestCase):
    def test_to_polar(self):
        self.assertEqual((pi/2, 1), Coords(0, 1).to_polar())
        self.assertEqual((0, 1), Coords(1, 0).to_polar())
        self.assertEqual((-pi/2, 1), Coords(0, -1).to_polar())
        self.assertEqual(3*pi/4, Coords(-1, 1).to_polar()[0])
        print(Coords(-1, 0).to_polar())

    def test_polar_with_ref(self):
        self.assertEqual((0, 1), Coords(2, 1).to_polar(ref=(1, 1)))

    def test_group_by_angle(self):
        self.assertEqual({0: [Coords(1, 0), Coords(2, 0)]}, group_by_angle(Coords(0, 0), [Coords(2, 0), Coords(1, 0)]))

    def test_index(self):
        self.assertEqual([[Coords(2, 1)], [Coords(1, 0)]], index_from_up({-pi: [Coords(2, 2)], -pi/2: [Coords(1, 1)], 0: [Coords(1, 0)], pi/2: [Coords(2, 1)]}))
