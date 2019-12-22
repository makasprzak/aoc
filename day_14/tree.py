import re

p = re.compile("([A-Z0-9]+)\)([A-Z0-9]+)")

class Analyzer:
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
    def __init__(self, product: str, component: str, amount: int):
        self.amount = amount
        self.product = product
        self.component = component

    def attach(self, other):
        self.previous = other

    def __eq__(self, o: object) -> bool:
        return (self.product, self.component, self.amount) == (o.product, o.component, o.amount)

    def __hash__(self) -> int:
        return (self.product, self.component, self.amount).__hash__()

    def __str__(self):
        if self.product is not None:
            return "{0} <-{1}- {1}".format(self.product, self.amount, self.component)
        else:
            return "ROOT"

    def __repr__(self):
        return self.__str__()


def to_list(leaf: Link):
    res = []
    while leaf.product is not None:
        res.append(leaf)
        leaf = leaf.previous
    return res


class Tree:
    def __init__(self):
        self.junctions = {Link(None, "FUEL", 1)}
        self.leaves = self.junctions.copy()

    def append(self, link: Link):
        found = False
        new_junctions = set()
        for junction in self.junctions:
            if junction.target == link.product:
                link.attach(junction)
                if junction.source is not None and self.leaves.__contains__(junction):
                    self.leaves.remove(junction)
                new_junctions.add(link)
                self.leaves.add(link)
                found = True
            if junction.source == link.component:
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
        analyzator = Analyzer()
        for leaf in self.leaves:
            res += analyzator.analyse(to_list(leaf))
        return res

    def find_leaf(self, target: str):
        for leaf in self.leaves:
            if leaf.component == target:
                return leaf

def build_tree(data):
    links = list(map(lambda x: parse(x), data))
    tree = Tree()
    for l in links:
        tree.append(l)
    return tree


def parse(element: str):
    m = p.match(element)
    return Link(m.group(1), m.group(2))