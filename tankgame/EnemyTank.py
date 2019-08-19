
from tankgame.MoveAble import *
from tankgame.BlockAble import *
from random import *
from tankgame.AutoFire import *
from tankgame.Bullet import *
from tankgame.SufferAble import *
from tankgame.DestroyAble import *
import time
import random
from tankgame.local import *

class EnemyTank(View, AutoMoveAble, MoveAble,AutoFire,BlockAble,SufferAble,DestroyAble):

    def __init__(self, **kwargs):
        super(EnemyTank, self).__init__(**kwargs, img='TankGame/img/p2tankD.gif')

        self.score = kwargs["score"]
        # 修改比较键
        self.comKey = 1
        # 所有的图片
        self.images = [
            pygame.image.load('TankGame/img/p2tankL.gif'),
            pygame.image.load('TankGame/img/p2tankR.gif'),
            pygame.image.load('TankGame/img/p2tankU.gif'),
            pygame.image.load('TankGame/img/p2tankD.gif')
        ]
        # 方向
        self.direction = Direction.DOWN
        # 移动速度
        self.speed = 0.5
        # 默认没有碰撞
        self.collision = False
        # 基准时间
        self.startTime = time.time()
        # 发射子弹的时间间隔
        self.limitTime = 1
        # 坦克血量
        self.blood = 1
        self.type = Type.enemytank

    def randomDirection(self,direction):

        # 生成随机数0-3
        index = randint(0,3)
        newDirection = direction
        if index==0:
            newDirection = Direction.LEFT
        elif index==1:
            newDirection = Direction.RIGHT
        elif index==2:
            newDirection = Direction.UP
        elif index==3:
            newDirection = Direction.DOWN

        # 判断随机生成的方向是否和碰撞方向一致
        if newDirection==direction:
            # 如果一致,重新生成
            return self.randomDirection(direction)
        else:
            # 如果不一致,可以返回
            return newDirection

    def autoMove(self):
        # 判断是否发生碰撞
        if self.collision:
            self.collision = False
            # 随机换一个方向
            self.direction = self.randomDirection(self.direction)
            return
        # 没有碰撞可以移动
        if self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed
        elif self.direction == Direction.LEFT:
            self.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed

        if self.x<0:
            self.x=0
        elif self.y<0:
            self.y=0
        elif self.y>WINDOW_HEIGHT-self.height:
            self.y=WINDOW_HEIGHT-self.height
        elif self.y>WINDOW_WIDTH-self.width:
            self.y=WINDOW_WIDTH-self.width
    def notifyCollision(self):
        # 发生碰撞
        self.collision = True


    def display(self):
        # 修改图片
        self.image = self.images[self.direction.value]
        # 显示
        self.window.blit(self.image,(self.x,self.y))

    def autoFire(self):
        curTime = time.time()
        # 时间差
        offsetTime = curTime-self.startTime
        if offsetTime>self.limitTime:
            # 修改基准时间
            self.startTime = curTime
            return Bullet(type=self.type,owner=self,tank_x=self.x, tank_y=self.y, tank_width=self.width, tank_height=self.height, window=self.window,
                          direction=self.direction)

    def notifySuffer(self,attackAble):
        # 判断是否是友军
        if not isinstance(attackAble.owner,EnemyTank):
            self.blood -= 1

    def needDestroy(self):
        if self.blood <= 0:
            self.score.score += 1
            self.__reset()
            return False
        return False

    def __reset(self):
        views = self.views
        self.image = pygame.image.load('TankGame/img/p2tankD.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        x = random.randint(0, 19 * BLOCK_SIZE)
        y = self.height
        moveList = list(filter(lambda view: isinstance(view, MoveAble), views))
        for move in moveList:
            if move is self:
                continue
            moveRect = pygame.Rect(move.x, move.y, move.width, move.height)
            selfRect = pygame.Rect(x, y, self.width, self.height)
            if moveRect.colliderect(selfRect):
                return
            else:
                self.blood = 3
                self.x = x
                self.y = y


    class Score():
        def __init__(self):
            self.score = 0

