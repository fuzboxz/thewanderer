from tkinter import Tk, Canvas, NW
from lib.Utility import loadImage


class GameWindow(object):
    def __init__(self, width=720, height=720):
        self.root = Tk()
        self.width = width
        self.height = height

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()


class GameMap(object):
    def __init__(self, canvas, map):
        self.canvas = canvas
        self.map = map
        self.wallXY = []  # stores xy coordinates of wall boundaries
        self.floor = loadImage("floor.gif")
        self.wall = loadImage("wall.gif")
        self.drawMap()

    def drawMap(self):
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
