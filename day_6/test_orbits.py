from unittest import TestCase
from day_6.orbits import orbits, parse, Link, find_santa
from line_reader import read_lines


class TestOrbits(TestCase):
    def test_orbits(self):
        self.assertEqual(1, orbits(["COM)A"]))
        self.assertEqual(3, orbits(["COM)A", "A)B"]))
        self.assertEqual(3, orbits(["A)B", "COM)A"]))
        self.assertEqual(2, orbits(["COM)A", "COM)B"]))
        self.assertEqual(5, orbits(["COM)A", "A)B", "A)C"]))
        self.assertEqual(15, orbits(["COM)A", "A)B", "A)C", "C)D", "D)E", "C)F"]))

    def test_parse(self):
        self.assertEqual(Link("COM", "A"), parse("COM)A"))
        self.assertEqual(Link("COM", "1A"), parse("COM)1A"))

    def test_run(self):
        lines = read_lines('./input.txt')
        print("count orbits:", orbits(lines))
        print("find santa:", find_santa(lines))

    def test_find_santa(self):
        self.assertEqual(0, find_santa(["COM)YOU", "COM)SAN"]))
        self.assertEqual(1, find_santa(["COM)YOU", "COM)B", "B)SAN"]))
        self.assertEqual(1, find_santa(["COM)SAN", "COM)B", "B)YOU"]))
        self.assertEqual(1, find_santa(["COM)A", "A)B", "B)YOU", "A)SAN"]))
