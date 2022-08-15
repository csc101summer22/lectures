class Point:
    """ A point in the Cartesian plane """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    def __eq__(self, other):
        return (type(other) == Point
                and self.x == other.x
                and self.y == other.y)
