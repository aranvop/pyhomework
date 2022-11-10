import pygame
from bullet import Bullet
from set import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group) -> None:
        super().__init__(group)
        self.group=group
        self.import_assets()
        self.status='right'
        self.frame_index=0
        self.image=self.animations[self.status][self.frame_index]
        self.rect=self.image.get_rect(center=pos)
        self.speed=360
        #移动
        self.direction=pygame.math.Vector2()
        self.pos=pygame.Vector2(self.rect.center)
        self.bulnum=0
        self.health=10
        self.xdis=30
        #self.health=10
        self.yyy1=playerfile(pygame.Vector2(self.pos.x,self.pos.y+20),all_sprites,0)
        self.yyy2=playerfile(pygame.Vector2(self.pos.x-self.xdis,self.pos.y),all_sprites,0)
        self.yyy3=playerfile(pygame.Vector2(self.pos.x+self.xdis,self.pos.y),all_sprites,0)
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

        #发射弹幕
    def shoot(self,dt):
        pos0=pygame.Vector2(self.pos)
        pos0.x+=self.xdis*2/3
        #pos0.x-=8
        #pos0.y-=10
        pos1=pygame.Vector2(self.pos)
        #pos1.x+=8
        #pos1.y-=10
        pos1.x-=self.xdis*2/3
        newBullet=Bullet(pos0,self.group,0)
        newBullet1=Bullet(pos1,self.group,0)
        newBullet1=Bullet(self.pos,self.group,0)

        #self.bulletlist.append(Bullet('./bullet/0.png',pos0,all_sprites))
        #self.bulletlist.append(Bullet('./bullet/0.png',pos1,all_sprites))
        pass
    def move(self,dt):
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()
        self.pos+=self.direction*self.speed*dt
        #print(self.direction)
        self.rect.center=self.pos

    def update(self,dt) :
        self.yyy1.pos=(self.pos.x,self.pos.y+self.xdis)
        self.yyy2.pos=(self.pos.x-self.xdis,self.pos.y)
        self.yyy3.pos=(self.pos.x+self.xdis,self.pos.y)
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
        #self.yyy1.pos=(pygame.Vector2(self.pos.x,self.pos.y+20),all_sprites,0)

# class Point(pygame.sprite.Sprite):
#     def __init__(self,pos,group) :
#         super().__init__(group)
#         self.image=pygame.image.load('./player/point.png').convert_alpha()
#         self.pos=(400,300)
#         self.rect=self.image.get_rect(center=pos)

#     def update(self,dt):
#         self.pos=playerlist[0].pos


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
            self.xdis=20
            self.speed=180
        else :
            self.xdis=30
            self.speed=360
        if keys[pygame.K_z]:
            #print('z')
            
            if self.yyy1.bulnum==12:
                self.yyy3.shoot(dt)
                self.yyy2.shoot(dt)
                self.yyy1.shoot(dt)
                self.yyy1.bulnum=0
            else:
                self.yyy1.bulnum+=1
            if(self.bulnum==6):
                self.bulnum=0
                self.shoot(dt)
            else :
                self.bulnum+=1
        else :
            
            pass

class playerfile(pygame.sprite.Sprite):
    def __init__(self,pos,group,num) -> None:
        super().__init__(group)
        self.num=num
        self.selectType()
        self.pos=pos
        self.angle=0
        self.import_assets()
        self.frame_index=0
        self.image=self.animations[self.type][self.frame_index]
        self.rect=self.image.get_rect(center=pos)
        self.bulnum=0
    def selectType(self):
        if self.num==0:
            self.type='yyy'
        elif self.num==1:
            self.type='bgl'
    def animate(self,dt):
        self.frame_index+=2*dt
        if  self.frame_index>=len(self.animations[self.type]):
            self.frame_index=0
        self.image=self.animations[self.type][int(self.frame_index)]
        self.angle-=10
    def rotate(self):
        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        self.image = pygame.transform.rotozoom(self.image, self.angle, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
    def draw_img(self, x, y, angle):
        rotated_image = pygame.transform.rotate(self.image, angle) 
        self.image.blit(rotated_image, rotated_image.get_rect(center=self.image.get_rect(topleft=(x, y)).center).topleft)
    def import_assets(self):
        self.animations={
            self.type:[]}
        for animation in self.animations.keys():
            full_path ='./player/playerfile/'+animation
            self.animations[animation]=import_folder(full_path) 
    def shoot(self,dt):
        pos0=pygame.Vector2(self.pos)
        #pos0.x-=8
        pos0.y-=10
        newBullet=Bullet(pos0,all_sprites,1)
        #newBullet1=Bullet(pos1,self.group,1)
    def rotatePivoted(self,pivot):
        # rotate the leg image around the pivot
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = pivot
        #return image, rect   
    def update(self,dt):
        #self.pos=pygame.Vector2(playerlist[0].pos.x,playerlist[0].pos.y)
        self.rect.center=self.pos
        self.animate(dt)
        self.rotate()
        
