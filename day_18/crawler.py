from coords import Coords, Direction
from day_18.tree import Branch


class Crawler:
    def __init__(self, pos: Coords, direction: Direction, world_map: dict, max_x: int, max_y: int):
        self.max_y = max_y
        self.max_x = max_x
        self.world_map = world_map
        self.dir = direction
        self.start_dir = direction
        self.start_pos = pos
        self.pos = pos
        self.counter = 0
        self.items = dict()
        self.current_parent = Branch(pos, direction, dict(), 0, None, [Direction.right(), Direction.left()])
        self.trace = set()
        self.root = self.current_parent

    def move(self):
        self.counter += 1
        self.pos += self.dir
        self.trace.add(self.pos)

    def read(self):
        value = self.world_map.get(self.pos, '.')
        if ord(value) in range(ord('a'), ord('z')) or ord(value) in range(ord('A'), ord('Z')):
            self.items[value] = self.counter
            return True
        return False

    def look_around(self):
        possibilities = [self.dir.turnLeft(), self.dir, self.dir.turnRight()]
        possibilities = list(filter(lambda dir: self.world_map.get(self.pos + dir, '.') not in '#@' and self.pos + dir not in self.trace, possibilities))
        return possibilities

    def crawl(self):
        while True:
            self.move()
            item_found = self.read()
            self.print()
            possibilities = self.look_around()
            if len(possibilities) == 1 and not item_found:
                self.dir = possibilities[0]
                continue
            elif len(possibilities) > 1 or (item_found and len(possibilities) > 0):
                last_parent = self.current_parent
                self.current_parent = Branch(self.start_pos, self.start_dir, self.items, self.counter, self.current_parent, possibilities)
                if last_parent is not None:
                    last_parent.children[self.start_dir] = self.current_parent
                self.start_pos = self.pos
                self.items = dict()
                self.counter = 0
                self.start_dir = possibilities[0]
                self.dir = self.start_dir
            else:
                if self.current_parent == None:
                    break
                self.current_parent.children[self.start_dir] = Branch(self.start_pos, self.start_dir, self.items, self.counter, self.current_parent, [])
                while True:
                    remaining_possibilities = list(filter(lambda dir: dir not in self.current_parent.children.keys(), self.current_parent.possibilities))
                    if len(remaining_possibilities) > 0:
                        self.start_dir = remaining_possibilities[0]
                        self.pos = self.start_pos
                        self.dir = self.start_dir
                        self.counter = 0
                        self.items = dict()
                        break
                    else:
                        self.start_pos = self.current_parent.root
                        self.current_parent = self.current_parent.parent
                        if self.current_parent is None:
                            return

    def print(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                coords = Coords(x, y)
                if self.pos == coords:
                    print('@', end='')
                elif coords in self.trace:
                    print('.', end='')
                else:
                    print(self.world_map.get(coords, ' '), end='')
            print()

