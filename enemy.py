import pygame
from set import *
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
        self.bullet=[]#子弹
        
        self.frame_index=0
        self.image=self.animations[self.status][self.frame_index]
        self.rect=self.image.get_rect(center=pos)
        self.speed=600
        #移动
        
        self.pos=pygame.Vector2(self.rect.center)
        self.direction=(400,600)-self.pos
        self.bulletlist=[]
        self.bulnum=1
        self.time=1
    def shoot(self,num):
        newBullet=enemyBullet(self.pos,all_sprites,num)
        newBullet.direction=playerlist[0].pos-self.pos

    def animate(self,dt):
        self.frame_index+=2*dt
        if  self.frame_index>=len(self.animations[self.status]):
            self.frame_index=0
        self.image=self.animations[self.status][int(self.frame_index)]
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
        if self.pos.y<0 or self.pos.y>600 or self.pos.x<0 or self.pos.x>800:
            #all_sprites.remove(self)
            enemylist.remove(self)
            self.kill()
            del self
    def update(self,dt):
        self.move(dt)
        self.animate(dt)
        self.tranBound()
        if self.time>0:
            #print(self.time)
            self.time-=dt
        else :
            self.time=0.5
            self.shoot(0)
        # if self.health<0:
        #     all_sprites.remove(self)
    def selecttype(self):
        if self.num==0:
            self.status='1left'
        elif self.num==1:
            self.status='1right'
        else :
            self.status='run'