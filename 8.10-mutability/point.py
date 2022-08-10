class Point:
    """ A point in the Cartesian plane """

    def __init__(self, x, y):
        # NOTE: These attributes, like all other variables, are mutable: they
        #        can be changed even after they are declared!
        #         * If an attribute is changed, should all other equal points
        #           also change in order to preserve equality?
        #         * If an attribute is changed, should only this point change,
        #           thereby breaking previously established equality?
        #       ...in Python, changing an attribute in one object will not
        #       change attributes in any other object, even if they were equal.
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    def __eq__(self, other):
        # NOTE: Without an eq method, the interpreter defaults to reference
        #       equality: two points are considered equal if and only if they
        #       occupy the same location in memory.

        # Two points are considered equal if and only if they are both Points
        #  and they have the same x- and y-coordinates:
        return (type(other) == Point
                and self.x == other.x
                and self.y == other.y)

pt1 = Point(3, 4)
pt2 = Point(3, 4)

def f(pt):
    pt.x = 5

f(pt1)
print(pt1)
print(pt2)
