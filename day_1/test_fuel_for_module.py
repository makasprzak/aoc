from unittest import TestCase

from day_1.fuel import fuel_for_mass, fuel_for_space_craft, fuel_for_module


class TestFuelForModule(TestCase):
    def test_fuel_for_mass(self):
        self.assertEqual(2, fuel_for_mass(12))
        self.assertEqual(2, fuel_for_mass(14))
        self.assertEqual(654, fuel_for_mass(1969))
        self.assertEqual(33583, fuel_for_mass(100756))

    def test_fuel_for_module(self):
        self.assertEqual(2, fuel_for_module(14))
        self.assertEqual(966, fuel_for_module(1969))
        self.assertEqual(50346, fuel_for_module(100756))

    def test_fuel_for_spacecraft(self):
        self.assertEqual(2 + 2 + 654 + 33583, fuel_for_space_craft(12, 14, 1969, 100756))
