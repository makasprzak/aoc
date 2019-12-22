from line_reader import parse_array


class Position:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def move(self, vector):
        return Position(self.x + vector.get('x'), self.y + vector.get('y'))

    def distance(self):
        return abs(self.x) + abs(self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        return str(self.x) + ":" + str(self.y)


def get_distance(instructions):
    positions = list(map(lambda line: process(line), instructions))
    positions = merge(positions[0], positions[1])
    distances = map(lambda p: p.distance(), positions)
    return min(distances)


def steps(instructions):
    positions = list(map(lambda line: process(line), instructions))
    print('processed positions')
    intersections = merge(set(positions[0]), set(positions[1]))
    print('merged intersections ' + str(len(intersections)))
    first = intersections_by_steps(set(intersections), positions[0])
    print('mapped first wire')
    second = intersections_by_steps(set(intersections), positions[1])
    print('mapped second wire')
    product = {}
    for k in first.keys():
        product[k] = first[k] + second[k]
    return min(product.values())


def intersections_by_steps(intersections: set, positions: list):
    res = {}
    i = 0
    for p in positions:
        i += 1
        if intersections.__contains__(p):
            res[p] = i
    return res

def process(line):
    return deduplicate(to_positions(to_vectors(parse_array(line))))


def deduplicate(positions):
    positions_set = set(positions.copy())
    deduplicated = []
    for p in positions:
        if positions_set.__contains__(p):
            deduplicated.append(p)
            positions_set.remove(p)
    return positions


def to_vectors(instructions):
    return map(lambda instruction: to_vector(instruction), instructions)


def merge(left: set, right: set):
    res = []
    for pos in left:
        if right.__contains__(pos):
            res.append(pos)
    return res


def to_vector(instruction):
    direction = instruction[0]
    return {
        'R': lambda n: {'x': n, 'y': 0},
        'L': lambda n: {'x': -n, 'y': 0},
        'U': lambda n: {'x': 0, 'y': n},
        'D': lambda n: {'x': 0, 'y': -n},
    }.get(direction)(int(instruction[1:]))


def to_positions(vectors):
    positions = [Position(0, 0)]
    for vector in vectors:
        position_trace = trace(positions[-1], vector)
        positions += position_trace
    return positions[1:]


def trace(last_position: Position, vector):
    xs = vector.get('x')
    if xs != 0:
        for x in range(0, abs(xs)):
            last_position = last_position.move({'x': xs / abs(xs), 'y': 0})
            yield last_position

    ys = vector.get('y')
    if ys != 0:
        for y in range(0, abs(ys)):
            last_position = last_position.move({'y': ys / abs(ys), 'x': 0})
            yield last_position
