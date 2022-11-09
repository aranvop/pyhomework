import pygame
from set import *
from support import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self,filename,pos,group:pygame.sprite.Group,num) :
        super().__init__(group)
        self.image=pygame.image.load(filename).convert_alpha()
        #self.image=pygame.transform.rotozoom(self.image,50,1)
        self.pos=pygame.Vector2(pos)
        self.direction=pygame.Vector2()
        self.speed=1500
        self.rect=self.image.get_rect(center=pos)        #self.direction=pygame.math.Vector2(0,1)
        self.direction.y=-1
        self.direction.x=0
        self.ishit=False
        #self.angle=0
    #def display():
    def move(self,dt):
        #self.pos+=self.direction*self.speed*dt
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt
        self.rect.center=self.pos
    #判断击中敌人
    def hit(self,enemylist):
        #print(enemylist)
        num=len(enemylist)
        i=0
        for i in enemylist:
            if self.pos.distance_squared_to(i.pos)<900:
                self.ishit=True
                i.health-=10
                if i.health<0:
                    enemylist.remove(i)
                    i.kill()
        if self.ishit==True:
            all_sprites.remove(self)   
            del self 

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
        if self.pos.y<0 or self.pos.y>600 or self.pos.x<0 or self.pos.x>800:
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
        self.selectType(num)
        self.import_assets()
        self.image=self.animations[self.mytype][self.frame_index]
        self.pos=pygame.Vector2(pos)
        self.direction=pygame.Vector2()
        self.speed=300
        self.angle=0
        self.rect=self.image.get_rect(center=pos)        #self.direction=pygame.math.Vector2(0,1)
        self.direction.y=1
        self.direction.x=1
    def selectType(self,num):
        if num==0:
            self.mytype="./bullet/star/"
        elif num==1:
            self.mytype="./bullet/bigbul/"
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
        if self.pos.distance_squared_to(playerlist[0].pos)<49:
            #print(playerpos)
            playerlist[0].health-=20
            print(playerlist[0].health)
            all_sprites.remove(self)
            del self

    def tranBound(self):
        if self.pos.y<0 or self.pos.y>600 or self.pos.x<0 or self.pos.x>800:
            all_sprites.remove(self)
            del self
    def animate(self,dt):
        #self.image=pygame.transform.rotozoom(self.image,30,1)
        self.angle-=2
        self.frame_index+=2*dt
        if  self.frame_index>=len(self.animations[self.mytype]):
            self.frame_index=0
        self.image=self.animations[self.mytype][int(self.frame_index)]
        self.image=pygame.transform.rotozoom(self.image,self.angle,1)
    def update(self,dt):
        self.move(dt)
        self.hit(playerlist)
        self.tranBound()
        self.animate(dt)





