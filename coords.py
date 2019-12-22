class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coords(self.x - other.x, self.y - other.y)

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

class Direction(Coords):
    def turnLeft(self):
        if self.x == 0:
            return Direction(self.y, self.x)
        else:
            return Direction(self.y, -self.x)

    def turnRight(self):
        if self.x == 0:
            return Direction(-self.y, self.x)
        else:
            return Direction(self.y, self.x)
