import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

from Point import Point
from Line import Line

class DrawingArea():

    def __init__(self):
        self.polygons = []

    def addBorders(self, left_bottom, right_top):
        self.left_bottom_border = left_bottom
        self.right_top_border = right_top

        left_top = Point(left_bottom.x, right_top.y)
        right_bottom = Point(right_top.x, left_bottom.y)
        
        self.borders = [
            Line(left_bottom, left_top),
            Line(left_top, right_top),
            Line(right_bottom, right_bottom),
            Line(right_bottom, left_bottom)
        ]

    def addPoly(self, poly):
        self.polygons.append(poly)


    def _drawLine(self, line):

        verts = [
            line.p1.getPointsTuple(),
            line.p2.getPointsTuple()
        ]

        codes = [
            Path.MOVETO,
            Path.LINETO
        ]

        return verts, codes


    def _drawBorders(self):

        verts = []
        codes = []
        for line in self.borders:
            add_verts, add_codes = self._drawLine(line)
            verts += add_verts
            codes += add_codes

        return Path(verts, codes)


    def draw(self):
        
        border_path = self._drawBorders()
        border_path = patches.PathPatch(border_path, edgecolor='red', lw=2)

        fig, ax = plt.subplots()
        ax.add_patch(border_path)
        ax.set_xlim(self.left_bottom_border.x, self.right_top_border.x)
        ax.set_ylim(self.left_bottom_border.y, self.right_top_border.y)
        plt.show()