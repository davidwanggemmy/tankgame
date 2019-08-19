from tankgame.Mytank import Mytank
from tankgame.Forest import Forest
from tankgame.Water import Water
from tankgame.BrickWall import BrickWall
from tankgame.Rock import Rock
from tankgame.EnemyTank import EnemyTank
from tankgame.local import *
from tankgame.host import *
import time
time_start = time.time()  # 开始计时
time_end = time.time()  # 结束计时
time_c = time_end - time_start


def parseMap(path, window, views, score):
    # 解析地图
    file = open(path, encoding='utf-8')
    # 全部读取
    lines = file.readlines()
    # 遍历每一行
    for row in range(0, len(lines)):
        line = lines[row]
        # 获取每一行字符
        for col in range(0, len(line)):
            str = line[col]
            if str == '主':
                # 创建我方坦克
                views.append(Mytank(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window,direction=Direction.UP))
            elif str == '草':
                views.append(Forest(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str == '水':
                views.append(Water(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str == '铁':
                views.append(Rock(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str=='砖':
                views.append(BrickWall(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str=='敌':
                views.append(EnemyTank(score=score, x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str=='堡':
                views.append(host(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))

    # 列表排序(坦克放到前面)
    views.sort(key=lambda view:view.comKey)