from Point import Point
from DrawingArea import DrawingArea

LEFT_BOTTOM = Point(0., 0.)
RIGHT_TOP = Point(50., 50.)

da = DrawingArea()
da.addBorders(LEFT_BOTTOM, RIGHT_TOP)
da.draw()


