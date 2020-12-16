from lib.Utility import loadImage
from lib.Character import Character


class Skeleton(Character):

    def __init__(self, canvas, xy):
        super().__init__(canvas)
        self.img = loadImage("skeleton.gif")
        self.x = xy[0]
        self.y = xy[1]
        self.Draw(self.img)
