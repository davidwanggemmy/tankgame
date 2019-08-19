from tankgame.MoveAble import *
from tankgame.Bullet import *
from tankgame.BlockAble import *
from tankgame.SufferAble import *
from tankgame.DestroyAble import *
from tankgame.View import *
# from tankgame.View import *

class Mytank(View, MoveAble,BlockAble,SufferAble,DestroyAble):
    def __init__(self, **kwargs):
        self.speed = 2.5
        self.direction = kwargs['direction']
        self.images = [
            pygame.image.load('TankGame/img/p1tankL.gif'),
            pygame.image.load('TankGame/img/p1tankR.gif'),
            pygame.image.load('TankGame/img/p1tankU.gif'),
            pygame.image.load('TankGame/img/p1tankD.gif')
        ]
        super(Mytank, self).__init__(**kwargs, img='TankGame/img/p1tankL.gif')
        self.comKey = 1
        self.image = self.images[self.direction.value]
        self.collision = False
        self.blood = 5
        self.type = Type.mytank

    def display(self):
        # 修改显示的图片
        self.image = self.images[self.direction.value]
        # 父类的display
        super(Mytank, self).display()

    def move(self, direction):

        # 如果移动的方向和原来的方向不一致,需要先换方向
        if self.direction != direction:
            self.direction = direction
            return
        if self.collision:
            self.collision = False
            return
        if direction == Direction.UP:
            self.y -= self.speed
        elif direction == Direction.DOWN:
            self.y += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.RIGHT:
            self.x += self.speed

    def notifyCollision(self):

        self.collision = True

    def fire(self):
        return Bullet(type=self.type,owner=self,tank_x=self.x, tank_y=self.y, tank_width=self.width, tank_height=self.height, window=self.window,
                      direction=self.direction)

    def notifySuffer(self,attackAble):
        if not isinstance(attackAble.owner,Mytank):
            self.blood -= 1

    def needDestroy(self):
        return self.blood<=0