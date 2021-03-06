from random import randint
from tkinter import Tk, Canvas, NW, N
from lib.Utility import loadImage


class GameWindow(object):
    def __init__(self, width=720, height=720):
        self.root = Tk()
        self.width = width
        self.height = height

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self._stats = Canvas(self.root, width=self.width, height="32")

        self.canvas.pack()
        self._stats.pack()

    def updateStats(self, hero):
        self._stats.delete("all")
        color = "white"
        if hero.hp <= 0:
            stats = "You are DEAD"
            color = "red3"
        else:
            stats = "HP: {5}/{0} |  DP: {1} | SP: {2} | Key: {3} | Level: {4}".format(hero.hp, hero.dp, hero.sp, hero.haskey, hero.level, hero.maxhp)
        self._stats.create_rectangle(0, 0, self.width, 30, fill=color)
        self._stats.create_text(self.width / 2, 7, font=("Arial bold", 12), text=stats, anchor=N)


class GameMap(object):
    def __init__(self, canvas, map):
        self.canvas = canvas
        self.map = map
        self.wallXY = []  # stores xy coordinates of wall boundaries
        self.floor = loadImage("floor.gif")
        self.wall = loadImage("wall.gif")
        self.drawMap()

    def drawMap(self):
        self.canvas.delete("all")
        x = 0
        y = 0

        for row in self.map:
            for tile in row:

                if tile == "0":
                    self.drawFloor(x, y)
                elif tile == "1":
                    self.drawWall(x, y)
                    self.wallXY.append([x, y])  # adds xy coordinates of wall boundaries to object

                x = x + 72
                if 720 <= x:
                    x = 0

            y = y + 72
            if 720 <= y:
                y = 0

    def drawFloor(self, x, y):
        self.canvas.create_image(x, y, anchor=NW, image=self.floor)

    def drawWall(self, x, y):
        self.canvas.create_image(x, y, anchor=NW, image=self.wall)

    @staticmethod
    def generateRandomMap():
        randmap = []
        for row in range(10):
            randmap.append([])
            for cell in range(10):
                randmap[row].append(str(0))
        wallsegments = randint(10, 15)  # nosec - not crypto, same for all below
        for i in range(wallsegments):
            while True:
                x = randint(0, 9)  # nosec
                y = randint(0, 9)  # nosec

                if [x, y] != [0, 0]:  # not on origin
                    randmap[x][y] = '1'
                    break
        return randmap
