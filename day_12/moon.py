import numpy as np
from copy import deepcopy
import re

from day_12.one_d_moon import DimensionAnalyzer, OneDMoon
from line_reader import read_lines

coord_pattern = re.compile("([xyz])=(\-?\d+)")


def compare(left, right):
    return np.sign(left - right)

class Coords:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return (self.x, self.y, self.z).__hash__()

    def __str__(self):
        return str(self.x) + ':' + str(self.y) + ':' + str(self.z)

    def __repr__(self):
        return self.__str__()

    def compare(self, other):
        return Coords(compare(other.x, self.x), compare(other.y, self.y), compare(other.z, self.z))

    def energy(self):
        return abs(self.x) +abs(self.y) + abs(self.z)


class Moon:
    def __init__(self, init_pos: Coords):
        self.pos = init_pos
        self.vel = Coords(0, 0, 0)

    def apply_gravities(self, moons: []):
        for moon in moons:
            self.apply_gravity(moon)

    def apply_gravity(self, moon):
        self.vel += self.pos.compare(moon.pos)

    def move(self, world: []):
        self.apply_gravities(world)
        self.pos += self.vel

    def total_energy(self):
        return self.pos.energy() * self.vel.energy()

    def __str__(self):
        return "pos={0} vel={1}".format(self.pos, self.vel)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.pos, self.vel) == (other.pos, other.vel)


def simulate_world(steps: int, moons: []):
    for _ in range(0, steps):
        simulate_time_unit(moons)

    total = 0
    for moon in moons:
        total += moon.total_energy()
    return total


def simulate_time_unit(moons):
    world = deepcopy(moons)
    for moon in moons:
        moon.move(world)


def parse_world(path="./input.data"):
    lines = read_lines(path)
    moons = list(map(lambda line: parse_moon(line), lines))
    return moons


def parse_moon(moon_str: str):
    matches = coord_pattern.findall(moon_str)
    coords_dict = {k: int(v) for k, v in matches}
    return to_moon(coords_dict)


def to_moon(coords_dict):
    coords = Coords(int(coords_dict['x']), int(coords_dict['y']), int(coords_dict['z']))
    return Moon(coords)


def find_cycle_time(moons):
    i = 0
    last_x_cycles = [0,0,0,0]
    init_state = deepcopy(moons)
    while i == 0 or not np.array_equal(init_state, moons):
        for m in range(0, 4):
            if moons[m] == init_state[m]:
                print("moon {0} returned to initial state after {1}".format(m, i))
            if moons[m].pos == init_state[m].pos:
                print("moon {0} returned to initial POSITION after {1}".format(m, i))
            if moons[m].pos.x == init_state[m].pos.x and moons[m].vel.x == init_state[m].pos.x:
                print("moons {0} X returned to initial POSITION after {1}".format(m, i - last_x_cycles[m]))
                last_x_cycles[m] = i
        simulate_time_unit(moons)
        if (i % 1000000) == 0:
            print(moons)
        i += 1
    return i

def equal(left, right):
    return np.array_equal(left, right)



if __name__ == '__main__':
    # world = parse_world()
    # DimensionAnalyzer(list(map(lambda m:OneDMoon(m.pos.x), world))).start()
    # DimensionAnalyzer(list(map(lambda m:OneDMoon(m.pos.y), world))).start()
    # DimensionAnalyzer(list(map(lambda m:OneDMoon(m.pos.z), world))).start()
    print(np.lcm.reduce([102356, 116328, 231614]))


