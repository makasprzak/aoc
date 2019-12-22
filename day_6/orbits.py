import re

class Analyzator:
    def __init__(self):
        self.cache = set()

    def analyse(self, data):
        i = 0
        for element in data:
            if element in self.cache:
                i+=1
            else:
                break
        data = data[i:]
        if len(data) > 0:
            self.cache.add(data[0])
            return len(data) + self.analyse(data[1:])
        else:
            return 0


class Link:
    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target

    def attach(self, other):
        self.previous = other

    def __eq__(self, o: object) -> bool:
        return (self.source, self.target) == (o.source, o.target)

    def __hash__(self) -> int:
        return (self.source, self.target).__hash__()

    def __str__(self):
        if self.source is not None:
            return self.source + '->' + self.target
        else:
            return "ROOT"

    def __repr__(self):
        return self.__str__()


def to_list(leaf: Link):
    res = []
    while leaf.source is not None:
        res.append(leaf)
        leaf = leaf.previous
    return res


class Tree:
    def __init__(self):
        self.junctions = {Link(None, "COM")}
        self.leaves = self.junctions.copy()

    def append(self, link: Link):
        found = False
        new_junctions = set()
        for junction in self.junctions:
            if junction.target == link.source:
                link.attach(junction)
                if junction.source is not None and self.leaves.__contains__(junction):
                    self.leaves.remove(junction)
                new_junctions.add(link)
                self.leaves.add(link)
                found = True
            if junction.source == link.target:
                junction.attach(link)
                new_junctions.add(link)
                if link in self.leaves:
                    self.leaves.remove(link)
                found = True
        if not found:
            new_junctions.add(link)
            self.leaves.add(link)
        self.junctions = self.junctions | new_junctions

    def analyze(self):
        res = 0
        analyzator = Analyzator()
        for leaf in self.leaves:
            res += analyzator.analyse(to_list(leaf))
        return res

    def find_leaf(self, target: str):
        for leaf in self.leaves:
            if leaf.target == target:
                return leaf


def orbits(data: []):
    tree = build_tree(data)
    return tree.analyze()


def build_tree(data):
    links = list(map(lambda x: parse(x), data))
    tree = Tree()
    for l in links:
        tree.append(l)
    return tree


def parse(element: str):
    p = re.compile("([A-Z0-9]+)\)([A-Z0-9]+)")
    m = p.match(element)
    return Link(m.group(1), m.group(2))


def find_santa(data: []):
    tree = build_tree(data)
    santa = to_list(tree.find_leaf("SAN"))
    you = to_list(tree.find_leaf("YOU"))
    for s in range(0, len(santa)):
        for y in range(0, len(you)):
            if santa[s].source == you[y].source:
                return y + s
