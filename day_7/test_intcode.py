from unittest import TestCase
from day_5.intcode import intcode, decode_opcode


class TestIntcode(TestCase):
    def test_intcode(self):
        self.assertEqual([2, 0, 0, 0, 99],
                         intcode("1, 0, 0, 0, 99"))
        self.assertEqual([1, 3, 2, 5, 99],
                         intcode("1, 3, 2, 3, 99"))
        self.assertEqual([2, 3, 0, 6, 99],
                         intcode("2, 3, 0, 3, 99"))
        self.assertEqual([2, 4, 4, 5, 99, 9801],
                         intcode("2, 4, 4, 5, 99, 0"))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99],
                         intcode("1, 1, 1, 4, 99, 5, 6, 0, 99"))
        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
                         intcode("1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50"))

    def test_decode_opcode(self):
        self.assertEqual((1, 1, 1), decode_opcode(1101))
        self.assertEqual((1, 1, 2), decode_opcode(1102))
        self.assertEqual((1, 0, 2), decode_opcode(1002))
        self.assertEqual((0, 1, 2), decode_opcode(102))
        self.assertEqual((0, 0, 1), decode_opcode(1))