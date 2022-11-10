import pygame
from set import *
from support import *
class Item(pygame.sprite.Sprite):
    def __init__(self,pos,group,num):
        super().__init__(group)
        self.num=num
        self.isintake=False
        self.selecttype()
        self.group=group
        self.import_assets()
        self.frame_index=0
        self.image=self.animations[self.status][self.frame_index]
        self.rect=self.image.get_rect(center=pos)
        self.speed=400
        #移动
        self.pos=pygame.Vector2(self.rect.center)
        self.direction=pygame.Vector2(0,1)
    def selecttype(self):
        if self.num==0:
           self.status='p'
        elif self.num==1:
            self.status='d'
        else :
            self.status='p'
    def getAll(self):
        if playerlist[0].pos.y<200:
            self.speed=800
            self.direction=playerlist[0].pos-self.pos
    def import_assets(self):
        self.animations={
            self.status:[]}
        for animation in self.animations.keys():
            full_path ='./item/'+animation
            self.animations[animation]=import_folder(full_path)
            #键盘输入
    def intake(self):
        if self.isintake==True:
            # global power
            # power+=0.1
            # print(power)
            #self.kill()
            self.take()
            all_sprites.remove(self)
            del self
    def take(self):
        if self.num==0:
            global power
            power+=1
            print (power/100 )
        elif self.num==1:
            global score
            score +=10
    def move(self,dt):
        if self.pos.distance_squared_to(playerlist[0].pos)<2500:
            self.direction=playerlist[0].pos-self.pos
        if self.pos.distance_squared_to(playerlist[0].pos)<400:
            self.isintake=True
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt
        self.rect.center=self.pos
    def tranBound(self):
        if self.pos.y<0 or self.pos.y>600 or self.pos.x<0 or self.pos.x>800:
            all_sprites.remove(self)
            del self
    def update(self,dt):
        self.move(dt)
        self.getAll()
        self.tranBound()
        self.intake()