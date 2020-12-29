from random import randint
from lib.Graphics import GameMap, GameWindow
from lib.Hero import Hero
from lib.Boss import Boss
from lib.Skeleton import Skeleton
from lib.Utility import findEmptyCell, loadMap


class GameLoop(object):

    def __init__(self, width, height):
        # Initialize tk
        self.gw = GameWindow(width=width, height=height)

        # Load map00
        self.map = GameMap(self.gw.canvas, loadMap("01.txt"))
        self.gw.canvas.bind("<KeyPress>", self.keypress)
        self.gw.canvas.focus_set()
        self.hero = Hero(self.gw.canvas)
        self.nonempty = []
        self.nonempty += self.map.wallXY

        # Generate first batch of enemies
        self.generateEnemies(1)

        # Update stats
        self.gw.updateStats(self.hero)

        # Start tk loop
        self.gw.root.mainloop()

    def keypress(self, e):
        if (self.hero.hp > 0):
            if e.keycode == 87:   # W
                self.hero.Move(self.hero.x, self.hero.y - 72, self.map.wallXY)
            elif e.keycode == 83:  # S
                self.hero.Move(self.hero.x, self.hero.y + 72, self.map.wallXY)
            elif e.keycode == 65:  # A
                self.hero.Move(self.hero.x - 72, self.hero.y, self.map.wallXY)
            elif e.keycode == 68:  # D
                self.hero.Move(self.hero.x + 72, self.hero.y, self.map.wallXY)
            elif e.keycode == 32:
                self.hero.Strike(self.enemies)
                if not any(isinstance(enemy, Boss) for enemy in self.enemies) and self.hero.haskey:
                    self.nextLevel(self.hero.level + 1)
                self.gw.updateStats(self.hero)

    # generate a bunch of enemies
    def generateEnemies(self, level):
        self.enemies = []
        keyexists = False
        for i in range(3):
            enemyXY = findEmptyCell(self.nonempty)
            if (keyexists is False and (randint(0, 1) or i == 2)):  # nosec - not cryptorandom
                self.enemies.append(Skeleton(self.gw.canvas, enemyXY, level=level, haskey=True))
                keyexists = True
            else:
                self.enemies.append(Skeleton(self.gw.canvas, enemyXY, level=level))
            self.nonempty.append(enemyXY)

        # Generate boss
        bossXY = findEmptyCell(self.nonempty)
        self.enemies.append(Boss(self.gw.canvas, bossXY, level=level))
        self.nonempty.append(bossXY)

    # level up
    def nextLevel(self, level):
        self.enemies = []
        self.nonempty = []
        self.nonempty += self.map.wallXY
        self.hero.LevelUp()
        self.generateEnemies(level)

gl = GameLoop(720, 720)
