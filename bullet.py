import pygame
from set import *
from support import *
from item import *
from math import atan2 , degrees , pi
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,group:pygame.sprite.Group,num) :
        super().__init__(group)
        self.pos=pygame.Vector2(pos)
        self.num=num
        self.direction=pygame.Vector2()
        self.selectType()
        self.import_assets()
        self.seldir()
        self.frame_index=0
        self.image=self.animations[self.type][self.frame_index]
        self.image1=self.animations[self.type][self.frame_index]
        #self.image=pygame.image.load(filename).convert_alpha()
        #self.image=pygame.transform.rotozoom(self.image,50,1)
        self.image=pygame.transform.rotozoom(self.image1,-self.degs, 1)

        
        self.speed=1500
        self.rect=self.image.get_rect(center=pos)        #self.direction=pygame.math.Vector2(0,1)

        self.ishit=False
        #self.angle=0
    #def display():
    def selectType(self):
        if self.num==0:
            self.type="normal"
            self.direction.y=-1
            self.direction.x=0
        elif self.num==1:
            self.type='zhuizong'
            try:  
                self.direction=enemylist[0].pos-self.pos
            except:
                self.direction.y=-1
                self.direction.x=0
                
    def seldir(self):
        #if self.num==1:
            x=self.direction.x
            y=self.direction.y
            rad=atan2(y,x)
            rad%=2*pi
            self.degs=degrees(rad)
    def move(self,dt):

        if self.num==1:
            try:  
                self.direction=enemylist[0].pos-self.pos
            except:
                pass
            x=self.direction.x
            y=self.direction.y
            rad=atan2(y,x)
            rad%=2*pi
            degs=degrees(rad)
            self.image=pygame.transform.rotozoom(self.image1,-degs, 1)
        #self.pos+=self.direction*self.speed*dt
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt
        self.rect.center=self.pos
    #判断击中敌人
    def hit(self,enemylist):
        #print(enemylist)
        num=len(enemylist)
        for i in enemylist:
            if self.pos.distance_squared_to(i.pos)<900:
                self.ishit=True
                i.health-=10
                if i.health<0:
                    i.creatItem()
                    enemylist.remove(i)
                    i.kill()
        if self.ishit==True:
            all_sprites.remove(self)   
            del self 
    def import_assets(self):
        self.animations={
            self.type:[]}
        for animation in self.animations.keys():
            full_path ='./bullet/'+animation
            self.animations[animation]=import_folder(full_path)
            #键盘输入
        # while (i<num):
        #     if self.pos.distance_squared_to(enemylist[i].pos)<400:
        #         enemylist[i].health-=10
        #         if enemylist[i].health<0:
        #             enemylist[i].pos=(-100,-100)
        #             enemylist[i].kill()
        #             enemylist[i].remove()
        #         all_sprites.remove(self)
        #         del self

        #     i+=1
        #判断越界
    def tranBound(self):
        if self.pos.y<0 or self.pos.y>750 or self.pos.x<0 or self.pos.x>700:
            all_sprites.remove(self)
            del self
    def update(self,dt):
        
        self.move(dt)
        self.hit(enemylist)
        self.tranBound()



class enemyBullet(pygame.sprite.Sprite):
    def __init__(self,pos,group:pygame.sprite.Group,num) :
        super().__init__(group)
        self.frame_index=0
        self.num=num
        self.selectType(num)
        self.import_assets()
        self.image=self.animations[self.mytype][self.frame_index]
        self.pos=pygame.Vector2(pos)
        self.direction=pygame.Vector2()
        self.speed=300
        self.angle=0
        self.rect=self.image.get_rect(center=pos)        #self.direction=pygame.math.Vector2(0,1)
        # self.direction.y=1
        # self.direction.x=1
    def selectType(self,num):
        if num==0:
            self.mytype="./bullet/star/"
            self.hitdis=49
        elif num==1:
            self.mytype="./bullet/yuan/"
            self.hitdis=49
        elif num==2:
            self.mytype="./bullet/bigbul/"
            self.hitdis=400
        elif num==3:
            self.mytype="./bullet/crowb/"
            self.hitdis=25         
    def move(self,dt):
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt
        self.rect.center=self.pos
    def import_assets(self):
        self.animations={
            self.mytype:[]}
        for animation in self.animations.keys():
            full_path =animation
            self.animations[animation]=import_folder(full_path)
            #键盘输入
    def hit(self,playerlist):
        #global playerpos
        global playerhealth
        if self.pos.distance_squared_to(playerlist[0].pos)<self.hitdis:
            #print(playerpos)
            playerlist[0].health-=20
            # print('youdead')
            # all_sprites.remove(self)
            # del self

    def tranBound(self):
        if self.pos.y<50 or self.pos.y>750 or self.pos.x<0 or self.pos.x>700:
            all_sprites.remove(self)
            del self
    def animate(self,dt):
        #self.image=pygame.transform.rotozoom(self.image,30,1)
        # self.angle-=2
        self.frame_index+=2*dt
        if  self.frame_index>=len(self.animations[self.mytype]):
            self.frame_index=0
        self.image=self.animations[self.mytype][int(self.frame_index)]
        # self.image=pygame.transform.rotozoom(self.image,self.angle,1)
    def update(self,dt):
        self.move(dt)
        self.hit(playerlist)
        self.tranBound()
        self.animate(dt)
        if self.num==0:
            self.rotate()
    def rotate(self):
        self.angle-=2
        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        self.image = pygame.transform.rotozoom(self.image, self.angle, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)





