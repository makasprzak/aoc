from unittest import TestCase
from day_3.crossed_wires import get_distance, to_vector, deduplicate, Position, merge, steps


class TestIntcode(TestCase):
    def test_crossed_wires(self):
        self.assertEqual(2, get_distance(["U1, R1", "R1, U1"]))
        self.assertEqual(3, get_distance(["U2, R1", "R1, U2"]))
        self.assertEqual(3, get_distance(["U2, R1", "R1, U3"]))
        self.assertEqual(2, get_distance(["U3, R2, D4", "R6"]))

    def test_crossed_wires_1(self):
        self.assertEqual(159, get_distance(["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]))

    def test_crossed_wires_2(self):
        self.assertEqual(135, get_distance(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]))

    def test_to_vector(self):
        self.assertEqual(to_vector('R1'), {'x': 1, 'y': 0})
        self.assertEqual(to_vector('R2'), {'x': 2, 'y': 0})
        self.assertEqual(to_vector('L2'), {'x': -2, 'y': 0})
        self.assertEqual(to_vector('U2'), {'x': 0, 'y': 2})
        self.assertEqual(to_vector('D2'), {'x': 0, 'y': -2})

    def test_deduplicate(self):
        self.assertEqual([Position(0, 0), Position(0,1)], deduplicate([Position(0, 0), Position(0,0), Position(0,1)]))

    def test_merge(self):
        self.assertEqual([Position(0, 1)], merge({Position(0, 0), Position(0, 1)}, {Position(0, 1), Position(1, 1)}))

    def test_steps(self):
        self.assertEqual(40, steps(["R10,U8,L6,D4", "U10,R8,D6,L4"]))
        self.assertEqual(610, steps(["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]))
        self.assertEqual(410, steps(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]))
