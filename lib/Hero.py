from lib.Character import Character
from lib.Skeleton import Skeleton
from lib.Utility import D6, loadImage


class Hero(Character):

    def __init__(self, canvas):
        super().__init__(canvas)

        self.hp = 20 + 3 * D6()
        self.dp = 2 * D6()
        self.sp = 5 + D6()
        self.level = 1
        self.haskey = False

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

    # overriden as hero can hit any enemy
    def Strike(self, enemies):
        enemy = ""
        for i in range(len(enemies)):
            if enemies[i].x == self.x and enemies[i].y == self.y:
                enemy = enemies[i]

        if (type(enemy) != str):
            damage = self.sp + D6() * 2
            print("Hero hitting ", type(enemy).__name__)
            print("Enemy health:", enemy.hp)
            print("Damage:", damage)
            if enemy.Hit(damage):
                print(type(enemy).__name__, " destroyed")
                enemies.remove(enemy)
                if isinstance(enemy, Skeleton) and enemy.haskey:
                    self.haskey = True
                    print("Got key!")
            else:

                enemy.Strike(self)


    # level up
    def LevelUp(self):
        self.haskey = False
        self.hp += D6()
        self.sp += D6()
        self.dp += D6()
        self.level += 1
