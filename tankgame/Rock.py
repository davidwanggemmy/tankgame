
from tankgame.BlockAble import *
from tankgame.View import *
from tankgame.SufferAble import *

class Rock(View,BlockAble,SufferAble):
    def __init__(self,**kwargs):
        super(Rock, self).__init__(**kwargs,img='TankGame/img/steels.gif')
