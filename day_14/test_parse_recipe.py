from unittest import TestCase
from day_14.fuel import Recipe, parse_recipe


class TestParseRecipe(TestCase):
    def test_parse_recipe(self):
        self.assertEqual(Recipe("FUEL", 1, {"ORE": 2}), parse_recipe("2 ORE => 1 FUEL"))
        self.assertEqual(Recipe("ABC", 2, {"ORE": 2, "A": 3}), parse_recipe("2 ORE, 3 A => 2 ABC"))
