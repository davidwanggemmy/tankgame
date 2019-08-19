import pygame
from enum import Enum

class Type(Enum):
    mytank = 0
    enemytank = 1
    other = 2



class View:
    def __init__(self,**kwargs):

        self.comKey = 2
        # 坐标
        self.x = kwargs['x']
        self.y = kwargs['y']
        # 图片Surface
        self.image = pygame.image.load(kwargs['img'])
        # window
        self.window = kwargs['window']
        # 宽度和高度
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.type = Type.other
    def display(self):
        self.window.blit(self.image,(self.x,self.y))

