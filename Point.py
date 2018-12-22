class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPointsTuple(self):
        return (self.x, self.y)

    @staticmethod
    def distance(cls, p1, p2):
        return ((p1.x - p2.x)**2 + (p1.y-p2.y)**2)**.5