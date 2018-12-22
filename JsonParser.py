import json
from Point import Point
from Polygon import Polygon

class JsonParser():

    def __init__(self, filename):
        with open(filename, 'r') as input_file:
            parsed_file = json.loads(input_file.read())
        
        self.start = Point(**parsed_file['start'])
        self.finish = Point(**parsed_file['finish'])
        self.polygons = [Polygon(**x) for x in parsed_file['polygons']]