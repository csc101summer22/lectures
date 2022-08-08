# Suppose we wish to represent the coordinates of a point -- if there are
#  multiple points, we have to be able to differentiate them:
x1 = 3
y1 = 4
x2 = 1
y2 = 2


# The interpreter has no idea that these are not four separate and independent
#  integers. It is now our responsibility to make sure that they are always
#  passed around and operated on together:
def translate(x, y, dx, dy):
    return x + dx, y + dy


x1, y1 = translate(x1, y1, 1, 1)
print(x1, y1)


# To define the new type "Point":
class Point:
    """ A point in the Cartesian plane """

    # Whenever a Point is created, its x- and y-coordinates must be specified.
    def __init__(self, x, y):
        # To set attributes within the current instance:
        self.x = x
        self.y = y

    # Whenever a Point is "stringified", its x- and y-coordinates should be
    #  included. As a rule of thumb, an object's string should always include
    #  enough information to recreate it.
    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)
