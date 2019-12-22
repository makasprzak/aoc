import re
import numpy as np
from line_reader import read_lines
from collections import Counter

p = re.compile("(\d+) ([A-Z]+)")

class Recipe:
    def __init__(self, product: str, amount: int, components: dict):
        self.product = product
        self.amount = amount
        self.components = components

    def __eq__(self, o: object) -> bool:
        return (self.product, self.amount) == (o.product, o.amount)

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __str__(self) -> str:
        return "{0} => {1} {2}".format(self.components, self.amount, self.product)

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return (self.product, self.amount).__hash__()



def parse_recipe(recipe_str: str) -> Recipe:
    elements = p.findall(recipe_str)
    elements = list(map(lambda e: (e[1], int(e[0])), elements))
    product = elements[-1]
    components = elements[0:-1]
    return Recipe(product[0], product[1], dict(components))


def count_ores(recipe_strings: []) -> int:
    recipes = map(parse_recipe, recipe_strings)
    recipes_by_products = {r.product: r for r in recipes}
    count = TreeAnalyzer().count_components("FUEL", 1, recipes_by_products)
    return count


def count_fuel(starting_needed_ore: int, recipe_strings: []) -> int:
    recipes = map(parse_recipe, recipe_strings)
    recipes_by_products = {r.product: r for r in recipes}
    analyzer = TreeAnalyzer({'ORE': 1000000000000})
    fuel = 0
    while True:
        delta_fuel = int(np.floor(analyzer.spares['ORE'] / starting_needed_ore))
        if delta_fuel == 0:
            delta_fuel = 1
        if analyzer.count_components("FUEL", delta_fuel, recipes_by_products) > 0:
            break
        else:
            fuel += delta_fuel
    return fuel


class TreeAnalyzer:
    def __init__(self, spares=dict()):
        self.spares = spares

    def use_spares(self, needed_product: str, needed_amt: int) -> int:
        existing_spare_count = self.spares.get(needed_product, 0)
        used_spares = existing_spare_count if needed_amt > existing_spare_count else needed_amt
        self.spares[needed_product] = self.spares.get(needed_product, 0) - used_spares
        return needed_amt - used_spares

    def count_components(self, needed_product: str, needed_amt: int, recipes: dict) -> (int, dict):
        recipe = recipes.get(needed_product)
        remaining_count = self.use_spares(needed_product, needed_amt)
        if needed_product == 'ORE':
            return remaining_count
        else:
            times = int(np.ceil(remaining_count / recipe.amount))
            spare_count = recipe.amount * times - remaining_count
            self.spares[needed_product] = self.spares.get(needed_product, 0) + spare_count
            ore_count = 0
            for component, amt in recipe.components.items():
                ore_count += self.count_components(component, amt * times, recipes)
            return ore_count


if __name__ == '__main__':
    lines = read_lines('./input.data')
    ores = count_ores(lines)
    print(ores)
    print(count_fuel(ores, lines))
    exit()
