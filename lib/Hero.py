from lib.Character import Character
from lib.Utility import D6, loadImage


class Hero(Character):

    def __init__(self, canvas):
        super().__init__(canvas)

        self.hp = 20 + 3 * D6()
        self.dp = 2 * D6()
        self.sp = 5 + D6()

        self.x = 0
        self.y = 0

        self.up = loadImage("hero-up.gif")
        self.down = loadImage("hero-down.gif")
        self.left = loadImage("hero-left.gif")
        self.right = loadImage("hero-right.gif")

        self.Draw(self.down)

    def Move(self, x, y, blocked):
        dir = self.down
        if x > self.x:
            dir = self.right
        elif x < self.x:
            dir = self.left
        elif y > self.y:
            dir = self.down
        elif y < self.y:
            dir = self.up

        if ([x, y] not in blocked):
            if (0 <= x < 720) & (0 <= y < 720):
                self.x = x
                self.y = y

        self.Draw(dir)
