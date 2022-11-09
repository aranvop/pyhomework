import pygame
from bullet import Bullet
from set import *
from support import *
class playerfile(pygame.sprite.Sprite):
    pass


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group) -> None:
        super().__init__(group)
        self.group=group
        self.import_assets()
        self.image1=pygame.image.load('./player/point.png').convert_alpha()
        self.bullet=[]#子弹
        self.status='right'
        self.frame_index=0
        self.image=self.animations[self.status][self.frame_index]
        self.rect=self.image.get_rect(center=pos)
        self.speed=360
        #移动
        self.direction=pygame.math.Vector2()
        self.pos=pygame.Vector2(self.rect.center)
        self.bulletlist=[]
        self.bulnum=1
        self.health=10
        #self.health=10
        #动画
    def animate(self):
        if  self.frame_index>=len(self.animations[self.status]):
            self.frame_index=len(self.animations[self.status])
        self.image=self.animations[self.status][int(self.frame_index)]

    def import_assets(self):
        self.animations={
            'up':[],'down':[],'left':[],'right':[]}
        for animation in self.animations.keys():
            full_path ='./player/'+animation
            self.animations[animation]=import_folder(full_path)
            #键盘输入
    def input(self,dt):
        keys =pygame.key.get_pressed()
        #if keys[pygame.K_LSHIFT or pygame.K_RSHIFT]:
            
        if keys[pygame.K_UP]:
            self.status='up'
            #不能超过边界：
            if self.pos.y >10:
                self.direction.y=-1
            else :
                self.direction.y=0
        elif keys[pygame.K_DOWN]:
            self.status='down'
            if self.pos.y <590:
                self.direction.y=1
            else :
                self.direction.y=0
        else:
            self.direction.y=0

        if keys[pygame.K_RIGHT]:
            self.status='right'
            if self.pos.x < 790:
                self.direction.x=1
            else :
                self.direction.x=0
        elif keys[pygame.K_LEFT]:
            self.status='left'
            if self.pos.x >10:
                self.direction.x=-1
            else :
                self.direction.x=0
            #self.direction.x=-1
        else:
            self.direction.x=0
            self.status='up'


        if keys[pygame.K_LSHIFT]:
            self.speed=180
        else :
            self.speed=360
        if keys[pygame.K_z]:
            #print('z')
            if(self.bulnum==6):
                self.bulnum=0
                self.shoot(dt)
            else :
                self.bulnum+=1
        else :
            pass
        #发射弹幕
    def shoot(self,dt):
        pos0=pygame.Vector2(self.pos)
        pos0.x-=8
        pos0.y-=10
        pos1=pygame.Vector2(self.pos)
        pos1.x+=8
        pos1.y-=10
        newBullet=Bullet('./bullet/0.png',pos0,self.group,0)
        newBullet1=Bullet('./bullet/0.png',pos1,self.group,0)

        #self.bulletlist.append(Bullet('./bullet/0.png',pos0,all_sprites))
        #self.bulletlist.append(Bullet('./bullet/0.png',pos1,all_sprites))
        pass
    def move(self,dt):
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt
        self.rect.center=self.pos

    def update(self,dt) :
        self.input(dt)
        self.move(dt)
        self.animate()
        global playerhealth
        global playerpos
        playerpos=self.pos
        if self.health<0:
            self.pos=(-200,-200)
            print("you dead")
            self.remove(all_sprites)

class Point(pygame.sprite.Sprite):
    def __init__(self,pos,group) :
        super().__init__(group)
        self.image=pygame.image.load('./player/point.png').convert_alpha()
        self.pos=(400,300)
        self.rect=self.image.get_rect(center=pos)

    def update(self,dt):
        self.pos=playerlist[0].pos
