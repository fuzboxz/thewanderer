from random import randint
from lib.Character import Character
from lib.Skeleton import Skeleton
from lib.Utility import D6, loadImage


class Hero(Character):

    def __init__(self, canvas):
        super().__init__(canvas)

        self.hp = 20 + 3 * D6()
        self.maxhp = self.hp
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

            print("\nHero vs {0}".format(type(enemy).__name__))

            while (enemy.hp >= 0 or self.hp >= 0):
                # Hero hits first
                damage = self.sp + D6() * 2

                print("Hero hitting ", type(enemy).__name__)
                print("Enemy health:", enemy.hp)
                print("Damage: {0} - {1} ".format(damage, enemy.dp))

                if enemy.Hit(damage):  # returns True if enemy was destroyed in the process
                    print(type(enemy).__name__, " destroyed")
                    enemies.remove(enemy)  # remove from list

                    if isinstance(enemy, Skeleton) and enemy.haskey:
                        self.haskey = True
                        print("Got key!")

                    return  # stop loop as enemy has been destroyed

                else:
                    enemy.Strike(self)
                    if self.hp <= 0:
                        return  # stop loop as hero died

    # level up
    def LevelUp(self):
        # prepare for new level
        self.level += 1
        self.x = 0
        self.y = 0
        self.haskey = False

        # level-up
        hp_roll = D6()
        self.hp += hp_roll
        self.maxhp += hp_roll
        self.sp += D6()
        self.dp += D6()

        # healing
        random = randint(0, 9)  # nosec
        prev = self.hp
        if (random < 5):  # 50% - 10% healing
            self.hp += int(self.maxhp * 0.1)
        elif (5 <= random < 9):  # 40% - 1/3 healing
            self.hp += int(self.maxhp * 0.3333)
        elif (random == 9):  # 10% - full recovery
            self.hp = self.maxhp
        if self.hp > self.maxhp:  # can't heal above max HP 
            self.hp = self.maxhp

        print("\nRestored {0} HP\n".format(abs(self.hp - prev)))

        self.Draw(self.down)
