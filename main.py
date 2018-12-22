from os import path

from Point import Point
from DrawingArea import DrawingArea
from JsonParser import JsonParser

JSON_FILENAME = 'input_data.json'

LEFT_BOTTOM = Point(0., 0.)
RIGHT_TOP = Point(50., 30.)

js = JsonParser(path.join('.', 'data', JSON_FILENAME))

da = DrawingArea(js.start, js.finish, js.polygons, LEFT_BOTTOM, RIGHT_TOP)
da.draw()


