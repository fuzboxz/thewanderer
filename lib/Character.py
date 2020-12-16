from abc import abstractmethod
from tkinter.constants import NW


class Character(object):

    def __init__(self, canvas):
        self.canvas = canvas
        self.id = -1  # -1 canvas id means that there is no object drawn on the canvas

    @abstractmethod
    def Move(self, x, y):
        pass

    @abstractmethod
    def Draw(self, img):
        if self.id != -1:  # there is an existing canvas id, so let's delete that first
            self.canvas.delete(self.id)
        self.id = self.canvas.create_image(self.x, self.y, anchor=NW, image=img)

    @abstractmethod
    def Delete(self):
        self.canvas.delete(self.id)
