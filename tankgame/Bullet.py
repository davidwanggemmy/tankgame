from tankgame.SufferAble import *
from tankgame.View import *
from tankgame.local import *
from tankgame.AutoMoveAble import *
from tankgame.DestroyAble import *
from tankgame.AttackAble import *
import pygame

class Bullet(View,AutoMoveAble,DestroyAble,AttackAble,SufferAble):
    def __init__(self, **kwargs):
        # 子弹拥有者
        self.owner = kwargs['owner']
        # 是否需要销毁
        self.shouldDestroy = False
        # 定义自动移动速度
        self.speed = 3
        # 获取方向属性
        self.direction = kwargs['direction']
        # 获取坦克属性
        tank_x = kwargs['tank_x']
        tank_y = kwargs['tank_y']
        tank_width = kwargs['tank_width']
        tank_height = kwargs['tank_height']
        # window
        self.window = kwargs['window']
        # 子弹图片
        self.image = pygame.image.load('TankGame/img/tankmissile.gif')
        # 宽度和高度
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.type = kwargs['type']

        # x和y
        if self.direction == Direction.UP:
            self.x = tank_x + tank_width / 2 - self.width / 2
            self.y = tank_y - self.height
        elif self.direction == Direction.DOWN:
            self.x = tank_x + tank_width / 2 - self.width / 2
            self.y = tank_y + tank_height
        elif self.direction == Direction.LEFT:
            self.x = tank_x - self.width
            self.y = tank_y + tank_height / 2 - self.height / 2
        elif self.direction == Direction.RIGHT:
            self.x = tank_x + tank_width
            self.y = tank_y + tank_height / 2 - self.height / 2

    def autoMove(self):
        if self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed
        elif self.direction == Direction.LEFT:
            self.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed

    def needDestroy(self):
        # 子弹越界
        return (self.x<0 or self.y<0 or self.x>WINDOW_WIDTH or self.y>WINDOW_HEIGHT) or self.shouldDestroy

    def hasCollision(self, sufferAble):
        # 坦克矩形(下一步的轨迹)
        if self.type == sufferAble.type:
            return False
        bulletRect = pygame.Rect(self.x, self.y, self.width, self.height)
        # 砖墙矩形
        sufferRect = pygame.Rect(sufferAble.x, sufferAble.y, sufferAble.width, sufferAble.height)
        # 边界碰撞结果
        return bulletRect.colliderect(sufferRect)

    def notifyAttack(self):

            self.shouldDestroy = True

    def notifySuffer(self, attack):
        if attack.owner != self.owner:
            self.shouldDestroy = True
