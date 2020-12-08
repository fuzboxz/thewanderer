from lib.Graphics import GameWindow, GameMap
from lib.Utility import loadMap


# Initialize tk
gw = GameWindow(width=720, height=720)

# Load map00
map = GameMap(gw.canvas, loadMap("00.txt"))
map.drawMap()

gw.root.mainloop()
