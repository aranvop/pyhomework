import pygame
import random
from set import *
from item import *
from support import *
from bullet import enemyBullet
class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,group,num):
        super().__init__(group)
        self.num=num
        self.selecttype()
        self.group=group
        self.import_assets()
        self.health=30
        self.frame_index=0
        self.image=self.animations[self.status][self.frame_index]
        self.rect=self.image.get_rect(center=pos)
        self.speed=600
        #移动
        self.pos=pygame.Vector2(self.rect.center)
        self.direction=(400,600)-self.pos
        self.time=1
    def shoot(self,num):
        newBullet=enemyBullet(self.pos,all_sprites,num)
        newBullet.direction=playerlist[0].pos-self.pos
        #图片更新
    def animate(self,dt):
        self.frame_index+=3*dt
        if  self.frame_index>=len(self.animations[self.status]):
            self.frame_index=0
        self.image=self.animations[self.status][int(self.frame_index)]
        #调取资源
    def import_assets(self):
        self.animations={
            self.status:[]}
        for animation in self.animations.keys():
            full_path ='./enemy/'+animation
            self.animations[animation]=import_folder(full_path)

            #键盘输入
    def  move(self,dt):
        # self.direction.y=2
        # self.direction.x=1
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt/8
        self.rect.center=self.pos
    def tranBound(self):
        if self.pos.y<-10 or self.pos.y>600+10 or self.pos.x<-10 or self.pos.x>810:
            #all_sprites.remove(self)
            enemylist.remove(self)
            self.kill()
            del self
    def update(self,dt):
        self.move(dt)
        self.animate(dt)
        self.tranBound()
        if self.num==0 or self.num==1:
            if self.time>0:
                self.time-=dt
            else :
                self.time=0.5
                self.shoot(0)
        elif self.num==2:
            if self.time>0:
                self.time-=dt
            else :
                self.time=2
                self.shoot(0)
        # if self.health<0:
        #     all_sprites.remove(self)
    def selecttype(self):
        if self.num==0:
            self.status='1left'
        elif self.num==1:
            self.status='1right'
        elif self.num==2:
            self.status='2bfd'
        elif self.num==9:
            self.status=='crino'
        else :
            self.status='run'
    def creatItem(self):
        if self.num==0 or self.num==1:
            item= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,1)
            item1= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,0)
        else :
            item= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,1)
            item1= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,0)