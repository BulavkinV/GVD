from Point import Point
from Line import Line

class Polygon():

    def __init__(self, x, y, vertices):
        self.internal_point = Point(x, y)
        self.lines = [ Line(Point(**p1), Point(**p2)) for p1, p2 in zip([vertices[-1]] + vertices[:-1], vertices) ]
