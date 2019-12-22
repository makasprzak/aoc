import numpy as np
from copy import deepcopy
from threading import Thread


def compare(left, right):
    return np.sign(left - right)


class OneDMoon:
    def __init__(self, init_pos: int):
        self.pos = init_pos
        self.vel = 0

    def apply_gravities(self, moons: []):
        for moon in moons:
            self.apply_gravity(moon)

    def apply_gravity(self, moon):
        self.vel += compare(moon.pos, self.pos)

    def move(self, world: []):
        self.apply_gravities(world)
        self.pos += self.vel

    def __str__(self):
        return "pos={0} vel={1}".format(self.pos, self.vel)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.pos, self.vel) == (other.pos, other.vel)


def simulate_time_unit(moons):
    world = deepcopy(moons)
    for moon in moons:
        moon.move(world)


def find_cycle_time(moons):
    i = 0
    init_state = deepcopy(moons)
    while i == 0 or not np.array_equal(init_state, moons):
        simulate_time_unit(moons)
        if (i % 100000) == 0:
            print(moons)
        i += 1
    return i

class DimensionAnalyzer(Thread):
    def __init__(self, moons):
        Thread.__init__(self)
        self.moons = moons

    def run(self) -> None:
        print("starting thread with ", self.moons)
        print("Found cycle: ", find_cycle_time(self.moons))

def equal(left, right):
    return np.array_equal(left, right)

