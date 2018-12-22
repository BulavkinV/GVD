import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

from Point import Point
from Line import Line
from Task import Task

class DrawingArea(Task):

    def __init__(self, start_point, end_point, obstacles, left_bottom, right_top):
        super(DrawingArea, self).__init__(start_point, end_point, obstacles, left_bottom, right_top)
        self.fig, self.ax = plt.subplots()

    def _generateLineImage(self, line):

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
            add_verts, add_codes = self._generateLineImage(line)
            verts += add_verts
            codes += add_codes

        return Path(verts, codes)

    def _drawObstacle(self, obstacle):
        verts = [obstacle.lines[0].p1.getPointsTuple()]
        code = [Path.MOVETO]
        for line in obstacle.lines[:-1]:
            verts.append(line.p2.getPointsTuple())
            code.append(Path.LINETO)

        verts.append(verts[0])
        code.append(Path.CLOSEPOLY)

        return Path(verts, code)        

    def redraw(self):
        """
            TODO
        """

        self.draw()

    def draw(self):

        plt.plot(self.start.x, self.start.y, 'bo')
        plt.plot(self.finish.x, self.finish.y, 'bo')

        border_path = self._drawBorders()
        border_path = patches.PathPatch(border_path, edgecolor='red', lw=2)
        self.ax.add_patch(border_path)

        obstacles_paths = [self._drawObstacle(x) for x in self.obstacles]
        for obstacle in obstacles_paths:
            self.ax.add_patch(
                patches.PathPatch(obstacle, edgecolor='black', facecolor='green', lw=2)
            )

        self.ax.set_xlim(self.left_bottom.x, self.right_top.x)
        self.ax.set_ylim(self.left_bottom.y, self.right_top.y)
        plt.show()

    