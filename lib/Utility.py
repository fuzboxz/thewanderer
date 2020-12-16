from os import path
from random import randint
from tkinter import PhotoImage


# get root directory of the game
def getRootFolder():
    root = path.dirname(path.dirname(path.realpath(__file__)))
    return root + path.sep


# load image from asset folder
def loadImage(asset):
    assetfolder = getRootFolder() + "assets" + path.sep
    return PhotoImage(file=assetfolder + asset)


# load map from filesystem
def loadMap(map_name):
    map_struc = []
    mappath = getRootFolder() + "map" + path.sep + map_name
    with open(file=mappath, mode="r") as f:
        for row in f.readlines():
            map_struc.append(row.replace("\n", "").split(sep=","))

    return map_struc


# generate xy based on the 72px grid system
def generateXY():
    return [randint(0, 9)*72, randint(0, 9)*72]  # nosec - not used for crypto


# find a cell that is not the origin, has no wall or other enemies
def findEmptyCell(filled):
    pos = generateXY()
    while(pos in filled or pos == [0, 0]):
        pos = generateXY()
    return pos


# roll a dice
def D6():
    return randint(1, 6)  # nosec - not used for crypto
