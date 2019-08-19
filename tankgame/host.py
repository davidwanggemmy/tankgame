from tankgame.BlockAble import BlockAble
from tankgame.DestroyAble import DestroyAble
from tankgame.SufferAble import SufferAble
from tankgame.View import View
import time

class host(View,BlockAble,SufferAble,DestroyAble):
    def __init__(self, **kwargs):
        super(host, self).__init__(**kwargs,img='TankGame/img/camp.gif')
        # 默认没有碰撞
        self.collision = False
        self.blood = 2
    def notifySuffer(self,attackAble):
        # 减少血量
        self.blood -= 1
    def needDestroy(self):
        return self.blood<=0