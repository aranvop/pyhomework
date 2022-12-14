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
        self.time=1
        self.time1=0.5
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

        self.bulangle=0
        self.bulangle1=3
        self.bulangle2=6
        self.bulangle3=9
    def selectTarget(self):
        if self.num==0 or self.num==1:
            self.direction=(400,600)-self.pos
        elif self.num==2 or self.num==3 or self.num==4 or self.num==5:
            self.target=pygame.Vector2(self.pos)
            self.target.y+=100
            self.direction=self.target-self.pos
        elif self.num==6:
            self.direction=(400,300)-self.pos
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
            if self.pos.y>200:
                if self.num==0:
                    self.direction.x=0.85
                else:
                    self.direction.x=-0.85
                self.speed=800
        elif self.num==2 or self.num==3 or self.num==4 or self.num==5:
            if self.target.distance_squared_to(self.pos)<9:
                self.direction=pygame.Vector2(0,0)
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt/6
        self.rect.center=self.pos
        
    def tranBound(self):
        if self.pos.y<-10 or self.pos.y>700+10 or self.pos.x<-10 or self.pos.x>810:
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
            self.health=400
        elif self.num==3 or self.num==4 or self.num==5:
           # self.bulnum=0
            self.speed=400
            self.status='2bfd'
            self.health=400
        elif self.num==6:
           # self.bulnum=0
            self.speed=1600
            self.status='crow'
            self.time=0.1
            self.time1=0.2
            self.health=20
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
        elif self.num==2 or self.num==3 or self.num==4 or self.num==5:
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
                    # self.time=1.5
                    # bulpos=pygame.Vector2(self.pos)
                    # bulpos.x+=20
                    # bulpos1=pygame.Vector2(self.pos)
                    # bulpos1.x-=20
                    # newBullet=enemyBullet(bulpos,all_sprites,1)
                    # newBullet.direction=playerlist[0].pos-self.pos
                    # #newBullet.direction.x+=10
                    # newBullet1=enemyBullet(bulpos1,all_sprites,1)
                    # newBullet1.direction=playerlist[0].pos-self.pos
        #螺旋弹
        elif self.num==2:
            if self.time1>0:
                self.time1-=dt
            else:
                if self.time>0:
                    self.time-=dt
                else :
                    self.time=0.001
                    self.bulangle+=0.5
                    self.bulangle1+=0.5
                    self.bulangle2+=0.5
                    self.bulangle3+=0.5
                    # self.bulangle+=12
                    # self.bulangle1+=12
                    newBullet=enemyBullet(self.pos,all_sprites,0)
                    newBullet1=enemyBullet(self.pos,all_sprites,0)
                    newBullet2=enemyBullet(self.pos,all_sprites,0)
                    newBullet3=enemyBullet(self.pos,all_sprites,0)
                    dir=pygame.Vector2(math.cos(self.bulangle*math.pi/6),math.sin(self.bulangle*math.pi/6))
                    dir1=pygame.Vector2(math.cos(self.bulangle1*math.pi/6),math.sin(self.bulangle1*math.pi/6))
                    newBullet.direction=pygame.math.Vector2(dir)
                    newBullet1.direction=pygame.math.Vector2(dir1)
                    newBullet2.direction=pygame.math.Vector2(math.cos(self.bulangle2*math.pi/6),math.sin(self.bulangle2*math.pi/6))
                    newBullet3.direction=pygame.math.Vector2(math.cos(self.bulangle3*math.pi/6),math.sin(self.bulangle3*math.pi/6))
                    self.bulnum+=2
                    if self.bulnum>60:
                        self.bulnum=0
                        self.time1=0.5
        #随机弹
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
        #三连弹
        elif   self.num==5:
            if self.time1>0:
                self.time1-=dt
            else:
                if self.time>0:
                    self.time-=dt
                else :
                    self.time=1
                    for i in range(12):
                        self.bulangle=i
                        print(self.bulangle,math.pi,math.cos(self.bulangle),math.sin(self.bulangle))
                        dir=pygame.Vector2(math.sin(math.pi*i/6+0.05),math.cos(math.pi*i/6+0.05))
                        newBullet1=enemyBullet(self.pos,all_sprites,1)
                        newBullet1.direction=pygame.math.Vector2(dir)
                        dir=pygame.Vector2(math.sin(math.pi*i/6-0.05),math.cos(math.pi*i/6-0.05))
                        newBullet2=enemyBullet(self.pos,all_sprites,1)
                        newBullet2.direction=pygame.math.Vector2(dir)
                        dir=pygame.Vector2(math.sin(math.pi*i/6),math.cos(math.pi*i/6))
                        newBullet=enemyBullet(self.pos,all_sprites,1)
                        newBullet.direction=pygame.math.Vector2(dir)
                    self.bulnum+=24
                    if self.bulnum>90:
                        self.bulnum=0
                        self.time1=3
        #四面八方
        elif   self.num==4:
            if self.time1>0:
                self.time1-=dt
            else:
                if self.time>0:
                    self.time-=dt
                else :
                    self.time=0.06
                    for i in range(24):
                        self.bulangle=i
                        dir=pygame.Vector2(math.sin(math.pi*i/12),math.cos(math.pi*i/12))
                        newBullet=enemyBullet(self.pos,all_sprites,1)
                        newBullet.direction=pygame.math.Vector2(dir)
                    self.bulnum+=24
                    if self.bulnum>90:
                        self.bulnum=0
                        self.time1=1
        if self.num==6:

            if self.time>0:
                self.time-=dt
            else :
                self.time=1
                newBullet=enemyBullet(self.pos,all_sprites,3)
                newBullet.direction=playerlist[0].pos-self.pos
                #self.bulnum+=1
