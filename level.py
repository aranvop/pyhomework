import pygame
#from settings import *
from bullet import Bullet
from player import *
from enemy import Enemy
from Time import Timer
from set import *
class Level :
    def __init__(self) :
        self.time=1
        self.display_surface=pygame.display.get_surface()
        self.all_sprites=pygame.sprite.Group()
        self.setup()
        self.image1=pygame.image.load('./bg2.png')
        self.image1=pygame.transform.scale(self.image1,(800,600),)
        self.image0=pygame.image.load('./moon.png')
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
        self.point=Point((0,0),all_sprites)
        #self.all_sprites.empty()
    def run(self,dt):
        self.display_surface.blit(self.image0,(0,0))#(pygame.image.load('./bg2.png'))
        self.display_surface.blit(self.image1,(0,0))
        self.all_sprites.draw(self.display_surface)
        all_sprites.draw(self.display_surface)

        self.all_sprites.update(dt)
        all_sprites.update(dt)
        if self.time>0:
            #print(self.time)
            self.time-=dt
        else :
            self.time=1
            self.creatEnemy((0,0),0)
            self.creatEnemy((800,0),1)