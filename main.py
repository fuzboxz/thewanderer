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

        self.hero = Hero(self.gw.canvas)

        # Start tk loop
        self.gw.root.mainloop()


gl = GameLoop(720, 720)