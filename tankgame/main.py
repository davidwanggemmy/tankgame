import random
import time

import pygame
from prompt_toolkit.layout import screen
from pygame import surface
from pygame.locals import *
from tankgame.utils import *
from tankgame.AutoFire import *
from tankgame.Mytank import *
from tankgame.utils import *
import sys
from tankgame.EnemyTank import *
import time

views = []




def start():
    # 初始化游戏
    pygame.init()


    # 显示窗口
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 修改游戏标题和图片
    pygame.display.set_caption("坦克大战")
    # 修改图标
    iconImage = pygame.image.load('TankGame/img/camp.gif')
    # 设置图标
    pygame.display.set_icon(iconImage)
    # 分数类
    score = EnemyTank.Score()
    font = pygame.font.Font("happy.ttf", 42)

    # 加载地图
    parseMap('TankGame/map/1.map', window, views, score)
    # 获取坦克
    tank = list(filter(lambda view: isinstance(view, Mytank), views))[0]
    host1 = list(filter(lambda view: isinstance(view,host), views))[0]
    enemytank = list(filter(lambda view: isinstance(view, EnemyTank), views))


    # 加载背景图片
    gameover=pygame.transform.scale(pygame.image.load("10.jpg"), (WINDOW_WIDTH, WINDOW_WIDTH))
    gamewin=pygame.image.load("11.jpg")

    text2 = ""
    # 死循环控制程序不退出
    fpsTime = 0
    while True:

        startTime = time.time()
        text = font.render('score: ' + str(score.score), True, (127, 255, 212))


        if tank.blood<=0 or host1.blood<0 :
            window.blit(gameover, (0, 0))

            window.blit(text, (40, 40))
            window.blit(text2, (40, 100))

            # 刷新窗口
            pygame.display.flip()

            # 处理事件
            eventList = pygame.event.get()

            for eventEle in eventList:
                if eventEle.type == QUIT:
                    # 退出游戏界面
                    pygame.quit()
                    # 退出程序
                    sys.exit()

        elif not list(filter(lambda enemy: enemy.blood > 0, enemytank)):
            window.blit(gamewin, (200,200))
            window.blit(text, (220, 220))
            window.blit(text2, (40, 100))
            # 刷新窗口
            pygame.display.flip()

            # 处理事件
            eventList = pygame.event.get()

            for eventEle in eventList:
                if eventEle.type == QUIT:
                    # 退出游戏界面
                    pygame.quit()
                    # 退出程序
                    sys.exit()

        else:


            # 检测自动发射的子弹
            autoFireList = list(filter(lambda view: isinstance(view, AutoFire), views))
            for autoFire in autoFireList:
                bullet = autoFire.autoFire()
                # 子弹发射有可能空弹
                if bullet:
                    # 添加到列表中
                    views.append(bullet)
            attackList = list(filter(lambda view: isinstance(view, AttackAble), views))
            sufferList = list(filter(lambda view: isinstance(view, SufferAble), views))
            for attack in attackList:
                for suffer in sufferList:
                        if attack != suffer:
                            collision = attack.hasCollision(suffer)
                            if collision:
                                attack.notifyAttack()
                                suffer.notifySuffer(attack)
                                break
            destroyList = list(filter(lambda view: isinstance(view, DestroyAble), views))
            for destroyView in destroyList:

                if destroyView.needDestroy():

                    destroyResult = destroyView.showDestroy()

                    if destroyResult:
                        views.append(destroyResult)

                    # 移除列表
                    views.remove(destroyView)
                    # 内存置为不可用
                    del destroyView

            # 处理自动移动
            # 获取所有自动移动的控件
            autoMoveList = list(filter(lambda view: isinstance(view, AutoMoveAble), views))
            for autoMove in autoMoveList:
                autoMove.autoMove()

            # 运动和阻挡碰撞检测
            # 运动的控件
            moveList = list(filter(lambda view: isinstance(view, MoveAble), views))
            # 阻挡的控件
            blockList = list(filter(lambda view: isinstance(view, BlockAble), views))
            # 运动和阻挡碰撞检测
            for move in moveList:
                for block in blockList:
                    # 如果是和自己碰撞,跳过去
                    if move == block:
                        continue
                    # 碰撞检测
                    collison = move.hasCollision(block)
                    if collison:
                        # 发生了碰撞
                        # 通知运动控件发生了碰撞
                        move.notifyCollision()
                        # 通知阻挡控件发生了碰撞
                        block.notifyCollision()
                        break
            # 清除窗口上的画面
            window.fill((0, 0, 0))
            time.sleep(0.01)
            fpsTime += 1
            if fpsTime >=0:

                fpsTime = -30
                endTime = time.time()
                offsetTime = endTime - startTime
                fps = (int(1 // offsetTime))
                text2 = font.render('FPs:' + str(fps), True, (127, 255, 212))

            # 显示所有的控件
            for view in views:
                view.display()
                window.blit(text, (40, 40))
                window.blit(text2, (40, 100))
            # 刷新
            pygame.display.flip()
            # 处理事件
            eventList = pygame.event.get()
            # 遍历事件
            for eventEle in eventList:
                if eventEle.type == QUIT:
                    # 退出游戏界面
                    pygame.quit()
                    # 退出程序
                    sys.exit()
                elif eventEle.type == KEYDOWN:
                    if eventEle.key == K_SPACE:
                        # 发生子弹
                        views.append(tank.fire())

            # 获取按压事件
            status = pygame.key.get_pressed()
            # 盘算是否有按键按压
            if 1 in status:
                # 有按键按压
                if status[K_a] or status[K_LEFT]:
                    tank.move(Direction.LEFT)
                elif status[K_d] or status[K_RIGHT]:
                    tank.move(Direction.RIGHT)
                elif status[K_w] or status[K_UP]:
                    tank.move(Direction.UP)
                elif status[K_s] or status[K_DOWN]:
                    tank.move(Direction.DOWN)



if __name__ == '__main__':
    start()
