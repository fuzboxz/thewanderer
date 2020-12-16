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

        # Generate skeletons
        self.enemies = []
        for i in range(3):
            enemyXY = findEmptyCell(self.nonempty)
            self.enemies.append(Skeleton(self.gw.canvas, enemyXY))
            self.nonempty.append(enemyXY)

        # Generate boss
        bossXY = findEmptyCell(self.nonempty)
        self.enemies.append(Boss(self.gw.canvas, bossXY))
        self.nonempty.append(bossXY)
        

        # Start tk loop
        self.gw.root.mainloop()

    def keypress(self, e):
        if e.keycode == 87:   # W
            self.hero.Move(self.hero.x, self.hero.y - 72, self.map.wallXY)
        elif e.keycode == 83:  # S
            self.hero.Move(self.hero.x, self.hero.y + 72, self.map.wallXY)
        elif e.keycode == 65:  # A
            self.hero.Move(self.hero.x - 72, self.hero.y, self.map.wallXY)
        elif e.keycode == 68:  # D
            self.hero.Move(self.hero.x + 72, self.hero.y, self.map.wallXY)


gl = GameLoop(720, 720)
