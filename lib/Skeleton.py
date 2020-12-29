from lib.Utility import loadImage
from lib.Character import Character
from lib.Utility import D6


class Skeleton(Character):

    def __init__(self, canvas, xy, level):
        super().__init__(canvas)
        self.img = loadImage("skeleton.gif")
        self.x = xy[0]
        self.y = xy[1]
        self.hp = 2 * level * D6()
        self.dp = level / 2 * D6()
        self.sp = level * D6()

        self.Draw(self.img)
