from Polygon import Polygon

class Task():

    def __init__(self, start_point, finish_point, obstacles, left_bottom, right_top):
        self.start = start_point
        self.finish = finish_point
        """
            TODO obstacles union
            TODO obstacles cut out of border
        """
        self.left_bottom = left_bottom
        self.right_top = right_top
        _constructBorder()

        obstacles = [self._cutObstacle(obstacle) for obstacle in obstacles]

        self.obstacles = obstacles

    def _constructBorder(self):
        left_top = Point(self.left_bottom.x, self.right_top.y)
        right_bottom = Point(self.right_top.x, self.left_bottom.y)
        
        self.border_lines = [
            Line(self.left_bottom, left_top),
            Line(left_top, self.right_top),
            Line(self.right_top, right_bottom),
            Line(right_bottom, self.left_bottom)
        ]

    def _cutObstalce(self, obstacle):
        for line in obstacle:
            for p in (line.p1, line.p2):
                if p.x < self.left_bottom.x or p.x > self.right_top.x:
                    # TODO

    def _getObstacles(self, obstacle):
        pass
    