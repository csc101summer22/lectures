import point


class Circle:
    """ A circle in the Cartesian plane """

    def __init__(self, x, y, radius):
        # It is possible for an attribute to be a reference:
        self.center = point.Point(x, y)
        self.radius = radius

    # By composing Points within Circles, operations on Circles can take
    #  advantage of the fact that Points already know how to operate on
    #  themselves.

    def __repr__(self):
        return "Circle(%r, %d)" % (self.center, self.radius)

    def __eq__(self, other):
        return (type(other) == Circle
                and self.center == other.center
                and self.radius == other.radius)

    # Some operations on Circles can simply delegate all of their
    #  responsibilities to the corresponding Point operations.

    def translate(self, dx, dy):
        self.center.translate(dx, dy)
