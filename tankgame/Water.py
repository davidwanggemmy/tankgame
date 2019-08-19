
from tankgame.BlockAble import *
from tankgame.View import *


class Water(View,BlockAble):
    def __init__(self,**kwargs):
        super(Water, self).__init__(**kwargs,img='TankGame/img/water.gif')
