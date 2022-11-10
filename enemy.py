import pygame
import random
from set import *
from item import *
from support import *
import math
from bullet import enemyBullet
class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,group,num):
        super().__init__(group)
        self.num=num
        self.selecttype()
        self.group=group
        self.import_assets()
        #self.health=50
        self.frame_index=0
        self.image=self.animations[self.status][self.frame_index]
        self.rect=self.image.get_rect(center=pos)
        self.bulnum=0
        #移动
        self.pos=pygame.Vector2(self.rect.center)
        # self.target=self.pos
        # self.target.y+=100
        self.selectTarget()
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.time=1
        self.time1=0.5
        self.bulangle=0
        self.bulangle1=180
    def selectTarget(self):
        if self.num==0 or self.num==1:
            self.direction=(400,600)-self.pos
        elif self.num==2 or self.num==3 or self.num==4:
            self.target=pygame.Vector2(self.pos)
            self.target.y+=100
            self.direction=self.target-self.pos
    # def shoot(self,num):
    #     newBullet=enemyBullet(self.pos,all_sprites,num)
    #     newBullet.direction=playerlist[0].pos-self.pos
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
        if self.num==0 or self.num==1:
            if self.pos.y>300:
                self.speed=400
        elif self.num==2 or self.num==3 or self.num==4:
            if self.target.distance_squared_to(self.pos)<9:
                self.direction=pygame.Vector2(0,0)
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt/6
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
        self.selectshoot()
    def selecttype(self):
        if self.num==0:
            self.status='1left'
            self.health=50
            self.speed=900
        elif self.num==1:
            self.status='1right'
            self.speed=900
            self.health=50  
        elif self.num==2:
            
            self.speed=400
            self.status='2bfd'
            self.health=600
        elif self.num==3:
           # self.bulnum=0
            self.speed=400
            self.status='2bfd'
            self.health=600
        elif self.num==4:
           # self.bulnum=0
            self.speed=400
            self.status='2bfd'
            self.health=600
        elif self.num==9:
            self.speed=600
            self.health=9999
            self.status=='crino'
        else :
            self.status='run'
    def creatItem(self):
        if self.num==0 or self.num==1:
            item= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,1)
            item1= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,0)
        elif self.num==2 or self.num==3 or self.num==4:
            for i in range(0,3):
                item= Item((self.pos.x+random.randint(-rang1,rang1),self.pos.y+random.randint(-rang1,rang1)),all_sprites,1)
                item1= Item((self.pos.x+random.randint(-rang1,rang1),self.pos.y+random.randint(-rang1,rang1)),all_sprites,0)
            # item2= Item((self.pos.x+random.randint(-rang1,rang1),self.pos.y+random.randint(-10,10)),all_sprites,1)
            # item3= Item((self.pos.x+random.randint(-rang1,rang1),self.pos.y+random.randint(-10,10)),all_sprites,0)             
        else :
            item= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,1)
            item1= Item((self.pos.x+random.randint(-10,10),self.pos.y+random.randint(-10,10)),all_sprites,0)

    def selectshoot(self):
        if self.num==0 or self.num==1:
            if self.time1>0:
                self.time1-=dt
            else:
                if self.time>0:
                    self.time-=dt
                else :
                    self.time=0.1
                    newBullet=enemyBullet(self.pos,all_sprites,1)
                    newBullet.direction=playerlist[0].pos-self.pos
                    self.bulnum+=1
                    if self.bulnum>5:
                        self.bulnum=0
                        self.time1=4
        elif self.num==2:
            if self.time1>0:
                self.time1-=dt
            else:
                if self.time>0:
                    self.time-=dt
                else :
                    self.time=0.01
                    self.bulangle+=12
                    self.bulangle1+=12
                    newBullet=enemyBullet(self.pos,all_sprites,0)
                    newBullet1=enemyBullet(self.pos,all_sprites,0)
                    dir=pygame.Vector2(math.cos(self.bulangle),math.sin(self.bulangle))
                    dir1=pygame.Vector2(math.cos(self.bulangle1),math.sin(self.bulangle1))
                    newBullet.direction=pygame.math.Vector2(dir)
                    newBullet1.direction=pygame.math.Vector2(dir1)
                    self.bulnum+=2
                    if self.bulnum>90:
                        self.bulnum=0
                        self.time1=2
        elif self.num==3:
            if self.time1>0:
                self.time1-=dt
            else:
                if self.time>0:
                    self.time-=dt
                else :
                    self.time=0.02
                    for i in range(5):
                        self.bulangle=random.randint(0,361)
                        dir=pygame.Vector2(math.cos(self.bulangle),math.sin(self.bulangle))
                        newBullet=enemyBullet(self.pos,all_sprites,0)
                        newBullet.direction=pygame.math.Vector2(dir)
                    self.bulnum+=5
                    if self.bulnum>180:
                        self.bulnum=0
                        self.time1=3
        elif   self.num==4:
            if self.time1>0:
                self.time1-=dt
            else:
                if self.time>0:
                    self.time-=dt
                else :
                    self.time=0.02
                    for i in range(5):
                        self.bulangle=random.randint(0,361)
                        dir=pygame.Vector2(math.cos(self.bulangle),math.sin(self.bulangle))
                        newBullet=enemyBullet(self.pos,all_sprites,0)
                        newBullet.direction=pygame.math.Vector2(dir)
                    self.bulnum+=5
                    if self.bulnum>180:
                        self.bulnum=0
                        self.time1=3
