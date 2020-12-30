from abc import abstractmethod
from tkinter.constants import NW
from lib.Utility import D6


class Character(object):

    def __init__(self, canvas):
        self.canvas = canvas
        self.id = -1  # -1 canvas id means that there is no object drawn on the canvas

    @abstractmethod
    def Move(self, x, y, blocked):
        if ([x, y] not in blocked):
            if (0 <= x < 720) & (0 <= y < 720):
                blocked.remove([self.x, self.y])
                self.x = x
                self.y = y
                blocked.append([x, y])
            else:
                return False
        else:
            return False

        self.Draw(self.img)

    @abstractmethod
    def Draw(self, img):
        if self.id != -1:  # there is an existing canvas id, so let's delete that first
            self.canvas.delete(self.id)
        self.id = self.canvas.create_image(self.x, self.y, anchor=NW, image=img)

    @abstractmethod
    def Delete(self):
        self.canvas.delete(self.id)

    @abstractmethod
    def Hit(self, damage):
        if damage < 0:
            damage = 0
        self.hp -= damage
        if (self.hp <= 0):
            self.Delete()
            return True
        else:
            return False

    @abstractmethod
    def Strike(self, enemy):
        damage = self.sp + D6() * 2
        print(type(self).__name__, " hitting Hero")
        print("Damage: {0} - {1} ".format(damage, enemy.dp))
        print("Hero health:", enemy.hp)
        enemy.Hit(damage - enemy.dp)
