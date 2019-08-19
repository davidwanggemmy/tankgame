
from tankgame.BlockAble import *
from tankgame.SufferAble import *

from tankgame.Blast import *

class BrickWall(View,BlockAble,SufferAble,DestroyAble):
    def __init__(self,**kwargs):
        super(BrickWall, self).__init__(**kwargs,img='TankGame/img/walls.gif')
        # 血量值
        self.blood = 3

    def notifySuffer(self,attackAble):
        # 减少血量
        self.blood -= 1

    def needDestroy(self):
        return self.blood<=0

    def showDestroy(self):
        return Blast(center_x=self.x+self.width/2,center_y=self.y+self.height/2,window=self.window)
