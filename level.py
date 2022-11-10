import pygame
#from settings import *
from bullet import Bullet
from player import *
from enemy import Enemy
from Time import Timer
from set import *
from item import *
class Level :
    def __init__(self) :
        self.time=1
        self.display_surface=pygame.display.get_surface()
        self.all_sprites=pygame.sprite.Group()
        self.setup()
        self.image1=pygame.image.load('./bg2.png')
        self.image1=pygame.transform.scale(self.image1,(800,600),)
        self.image0=pygame.image.load('./moon.png')
        self.lenum=0
        self.enemynum=0
        self.waitTime=1
        #self.image2=pygame.image.load('./player/point.png')
    #创建敌人
    def creatEnemy(self,pos,num):
        en=Enemy(pos,all_sprites,num)
        enemylist.append(en)

    def setup(self):
        self.player=Player((400,600),all_sprites)
        #self.time=Timer(10000,self.creatEnemy((0,0),0))
        #self.time.active
        #self.en=Enemy((-10,-10),all_sprites,0)
        playerlist.append(self.player)
        #enemylist.append(self.en)
        #self.item= Item((400,50),all_sprites,0)
        #self.point=playerfile((400,200),all_sprites,0)
        #self.all_sprites.empty()
    def run(self,dt):
        self.display_surface.blit(self.image0,(0,0))#(pygame.image.load('./bg2.png'))
        self.display_surface.blit(self.image1,(0,0))
        self.all_sprites.draw(self.display_surface)
        all_sprites.draw(self.display_surface)

        self.all_sprites.update(dt)
        all_sprites.update(dt)
        if self.waitTime>0:
            self.waitTime-=dt
        elif self.lenum==0 :
            if self.enemynum<60:
                if self.time>0:
                    #print(self.time)
                    self.time-=dt
                else :
                    self.time=0.5
                    self.creatEnemy((0,0),0)
                    self.creatEnemy((800,0),1)
                    self.enemynum+=2
            else:
                self.lenum=1
                self.waitTime=2
                self.enemynum=10


        #第二部分
        elif self.lenum==1:

            if self.enemynum<20:
                if self.enemynum%3!=0:
                    if self.time>0:
                        #print(self.time)
                        self.time-=dt
                    else :
                        self.time=2
                        #self.creatEnemy((0,0),0)
                        self.creatEnemy((400,0),3)
                        self.enemynum+=1
                else:
                    if self.time>0:
                        #print(self.time)
                        self.time-=dt
                    elif len(enemylist)==0 :
                        self.time=2
                        #self.creatEnemy((0,0),0)
                        self.creatEnemy((500,0),2)
                        self.creatEnemy((100,0),2)
                        self.enemynum+=1
            else:
                self.lenum=2
                self.waitTime=5
                self.enemynum=10
        elif self.lenum==2 and len(enemylist)==0:
            exit()
        # elif self.enemynum>=20:
        #     self.waitTime=2
        