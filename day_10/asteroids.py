from line_reader import read_lines
from math import sqrt, pow, copysign, atan, pi
from itertools import groupby
from numpy import arctan2
import numpy as np

def sign(x):
    return copysign(1, x)

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return (self.x, self.y).__hash__()

    def __str__(self):
        return str(self.x) + ':' + str(self.y)

    def __repr__(self):
        return self.__str__()

    def is_in_sight(self, other, map):
        for third in map:
            if other != self and third != self and third != other:
                if self.are_colinear(other, third) and self.distance(third) < self.distance(other) and sign(self.x - other.x) == sign(self.x - third.x) and sign(self.y - other.y) == sign(self.y - third.y):
                    return False
        return True

    def are_colinear(self, o1, o2):
        if self.x == o1.x and o1.x == o2.x:
            return True
        if self.x == o1.x and o1.x != o2.x:
            return False
        if self.x == o2.x and o1.x != o2.x:
            return False
        return (o1.y - self.y)/(o1.x - self.x) == (o2.y - self.y)/(o2.x - self.x)

    def distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def to_polar(self, ref=(0, 0)):
        x = self.x - ref[0]
        y = self.y - ref[1]
        # if x == 0:
        #     if y > 0:
        #         return pi/2, abs(y)
        #     else:
        #         return 3*pi/2, abs(y)
        # else:
        return arctan2(y, x), self.distance(Coords(ref[0], ref[1]))


def analyse(asteroids: []):
    counts = dict()
    print("Analyzing asteroids: " + str(len(asteroids)))
    for s in range(0, len(asteroids)):
        print('.', end='' if s % 50 else '\n', flush=True)
        for t in range(0, len(asteroids)):
            source = asteroids[s]
            target = asteroids[t]
            if source != target and source.is_in_sight(target, asteroids):
                existing = counts.get(source) or 0
                counts[source] = existing + 1
    print()
    return max(counts.items(), key=lambda c: c[1])


def group_by_angle(ref: Coords, asteroids: []) -> dict:
    groups = groupby(asteroids, key=lambda a: a.to_polar(ref=(ref.x, ref.y))[0])
    return {k: to_sorted_list(ref, v) for k, v in groups}


def to_sorted_list(ref: Coords, colinear_asteroids) -> []:
    l = list(colinear_asteroids)
    l.sort(key=lambda a: a.to_polar(ref=(ref.x, ref.y))[1])
    return l


def index_from_up(grouped_asteroids: dict) -> []:
    as_list = list(grouped_asteroids.items())
    as_list.sort(key=lambda el: sort_function(el))
    return list(map(lambda el: el[1], as_list))


def sort_function(el):
    f = el[0]
    phase = -pi/2
    return f if f >= phase else f + 2*pi


def lasers():
    parsed = parse()
    asteroid = analyse(parsed)[0]
    # asteroid = Coords(11,13)
    print("Best asteroid ", asteroid)
    asteroids = list(filter(lambda a: a != asteroid, parsed))
    grouped = group_by_angle(asteroid, asteroids)
    indexed = index_from_up(grouped)
    i = 0
    idxes = []
    for x in range(0, len(indexed)):
        idxes.append(0)
    while i < 200:
        g = i % len(indexed)
        if idxes[g] < len(indexed[g]):
            asteroid = indexed[g][idxes[g]]
            print("The {0}st asteroid to be vaporized is at {1},{2}".format(i + 1, asteroid.x, asteroid.y))
            idxes[g] += 1
            i += 1
    g = (i-1) % len(indexed)
    print("First one was ", indexed[0][0])
    return indexed[g][idxes[g] - 1]


def parse():
    lines = read_lines('./input.txt')
    map = []
    y = 0
    for line in lines:
        for x in range(0, len(line)):
            if line[x] == '#':
                map.append(Coords(x, y))
        y += 1
    return map

if __name__ == '__main__':
    # map = parse()
    # print(analyse(map))
    print(lasers())
