from lib.Hero import Hero
from lib.Graphics import GameWindow, GameMap
from lib.Utility import loadMap


class GameLoop(object):

    def __init__(self, width, height):
        # Initialize tk
        self.gw = GameWindow(width=width, height=height)

        # Load map00
        self.map = GameMap(self.gw.canvas, loadMap("01.txt"))
        self.map.drawMap()
        self.gw.canvas.bind("<KeyPress>", self.keypress)
        self.gw.canvas.focus_set()
        self.hero = Hero(self.gw.canvas)

        # Start tk loop
        self.gw.root.mainloop()

    def keypress(self, e):
        if e.keycode == 87:   # W
            self.hero.Move(self.hero.x, self.hero.y - 72)
        elif e.keycode == 83:  # S
            self.hero.Move(self.hero.x, self.hero.y + 72)
        elif e.keycode == 65:  # A
            self.hero.Move(self.hero.x - 72, self.hero.y)
        elif e.keycode == 68:  # D
            self.hero.Move(self.hero.x + 72, self.hero.y)


gl = GameLoop(720, 720)
