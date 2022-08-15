class Point:
    """ A point in the Cartesian plane """

    # NOTE: These three methods are sort of the bare minimum for a
    #       useful, readable class:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    def __eq__(self, other):
        return (type(other) == Point
                and self.x == other.x
                and self.y == other.y)

    # NOTE: We can also add additional methods implementing certain operators:

    def __add__(self, other):
        # The sum of two points is a new point consisting of the sums of
        #  their x- and y-coordinates:
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Cannot add a Point to an %r" % type(other))

    # NOTE: We can also add methods with no predefined purpose; by
    #       convention, these methods should not use double underscores,
    #       and will need to be called manually using '.':

    def translate(self, dx, dy):
        # We don't need to take x or y as arguments -- we already have them
        #  as our attributes. We also don't need to return the new x or y; we
        #  are simply modifying our own attributes.
        self.x = self.x + dx
        self.y = self.y + dy
