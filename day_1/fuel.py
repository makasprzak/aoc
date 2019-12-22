from functools import reduce
from math import floor


def fuel_for_mass(mass):
    return floor(mass / 3) - 2


def fuel_for_module(mass):
    fuel = 0
    while mass > 0:
        mass = fuel_for_mass(mass)
        fuel += mass if mass > 0 else 0
    return fuel


def fuel_for_space_craft(*masses):
    fuels = map(lambda mass: fuel_for_mass(mass), masses)
    return reduce(lambda x,y: x+y, fuels)


def fuel_for_space_craft_corrected(*masses):
    fuels = map(lambda mass: fuel_for_module(mass), masses)
    return reduce(lambda x, y: x+y, fuels)


def load_input():
    masses = []
    with open('./input.txt', 'r') as f:
        line = f.readline()
        while line:
            masses.append(int(line.strip()))
            line = f.readline()
    return masses
