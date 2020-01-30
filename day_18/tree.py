from coords import Coords, Direction


class Branch:
    def __init__(self, root: Coords, direction: Direction, items: [], steps: int, parent, possibilites: []):
        self.items = items
        self.children = dict()
        self.steps = steps
        self.parent = parent
        self.root = root
        self.direction = direction
        self.possibilities = possibilites

    def distance(self):
        steps = 0
        branch = self.parent
        while branch is not None:
            steps += branch.steps
            branch = branch.parent
        return steps
