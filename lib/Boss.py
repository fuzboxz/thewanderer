from lib.Utility import loadImage, D6
from lib.Character import Character


class Boss(Character):

    def __init__(self, canvas, xy, level):
        super().__init__(canvas)
        self.img = loadImage("boss.gif")
        self.x = xy[0]
        self.y = xy[1]
        self.hp = 200 * level * D6()
        self.dp = level / 2 * D6()
        self.sp = level * D6()

        self.Draw(self.img)
