import pygame
#from settings import *
from bullet import Bullet
from player import *
from enemy import Enemy
from Time import Timer
from set import *
from item import *
class Level :
    def __init__(self) :
        self.font =pygame.font.Font('./simsun.ttc',30)
        self.powtext=self.font.render('power:'+str(power/100),True,(255,255,255))
        self.scotext=self.font.render('点数:'+str(score/100),True,(255,255,255))
        self.time=1
        self.speed=0.1
        self.wapos=pygame.Vector2(-20,0)
        self.display_surface=pygame.display.get_surface()
        self.all_sprites=pygame.sprite.Group()
        self.setup()
        #self.image1=pygame.image.load('./bg2.png')
        self.image1=pygame.image.load('1.png').convert_alpha()
        self.image2=pygame.transform.scale(self.image1,(250,768),)
        self.image3=pygame.transform.scale(self.image1,(1000,18),)
        self.image1=pygame.transform.scale(self.image1,(1024,50),)
        self.image0=pygame.image.load('bg1.jpeg')
        self.image0=pygame.transform.scale(self.image0,(800,800),)
        self.lenum=0
        self.enemynum=0
        self.enemynum1=0
        self.waitTime=1
        self.zhong=False
        self.time2=0
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
        #self.item= Item((400,50),all_sprites,0)
        #self.point=playerfile((400,200),all_sprites,0)
        #self.all_sprites.empty()
    def run(self,dt):
        global power
        if self.wapos.x>0:
            self.speed=-0.1
        elif self.wapos.x<-50:
            self.speed=0.1
        self.wapos.x+=self.speed
        self.wapos.y+=self.speed
        self.display_surface.blit(self.image0,self.wapos)#(pygame.image.load('./bg2.png'))
        
        
        #self.display_surface.blit(self.image1,(0,50))
        self.all_sprites.draw(self.display_surface)
        all_sprites.draw(self.display_surface)

        self.all_sprites.update(dt)
        all_sprites.update(dt)
        self.display_surface.blit(self.image1,(0,0))
        self.display_surface.blit(self.image2,(700,50))
        self.display_surface.blit(self.image3,(0,750))
        str1=str(power)
        # print(power)
        self.powtext=self.font.render('power:'+str(self.player.power/100),False,(255,255,255))
        self.scotext=self.font.render('点数:'+str(self.player.score),True,(255,255,255))
        self.display_surface.blit(self.powtext,(800,600))
        self.display_surface.blit(self.scotext,(800,500))
        if self.waitTime>0:
            self.waitTime-=dt
        elif self.lenum==0 :
            if self.enemynum<60:
                if self.time>0:
                    #print(self.time)
                    self.time-=dt
                else :
                    self.time=0.5
                    self.creatEnemy((0,50),0)
                    self.creatEnemy((700,50),1)
                    self.enemynum+=2
                    if self.enemynum==30:
                        en=Enemy((350,50),all_sprites,5)
                        en.health=800
                        enemylist.append(en)
            else:
                self.lenum=1
                self.waitTime=2
                self.enemynum=0


        #第二部分
        elif self.lenum==1:

            if self.enemynum<20:

                if self.enemynum==5:
                    self.zhong=True
                if self.zhong==True:    
                    if self.enemynum1<10:
                        if self.time2>0:
                            #print(self.time)
                            self.time2-=dt
                        else :
                            self.time2=0.3
                            self.creatEnemy((0,300),6)
                            self.creatEnemy((700,300),6)
                            self.enemynum1+=2
                    else:
                        self.zhong=False
                        self.enemynum1=0

                if self.enemynum%2!=0:
                    if self.time>0:
                        #print(self.time)
                        self.time-=dt
                    else :
                        self.time=2
                        #self.creatEnemy((0,0),0)
                        self.creatEnemy((400,50),4)
                        self.enemynum+=1
                else:
                    if self.time>0:
                        #print(self.time)
                        self.time-=dt
                    elif len(enemylist)==0 :
                        self.time=2
                        #self.creatEnemy((0,0),0)
                        self.creatEnemy((500,50),3)
                        self.creatEnemy((100,50),2)
                        self.enemynum+=1
                        
            else:
                self.lenum=2
                self.waitTime=5
                self.enemynum=0


        elif self.lenum==2 :
            if self.enemynum<30:
                if self.time>0:
                    #print(self.time)
                    self.time-=dt
                else :
                    self.time=0.3
                    self.creatEnemy((0,300),6)
                    self.creatEnemy((700,300),6)
                    self.enemynum+=2
                    # if self.enemynum==30:
                    #     en=Enemy((350,50),all_sprites,5)
                    #     en.health=800
                    #     enemylist.append(en)
            else:
                self.lenum=1
                self.waitTime=2
                self.enemynum=10

        elif self.lenum==2 and len(enemylist)==0:
            self.lenum=0
            #exit()
        # elif self.enemynum>=20:
        #     self.waitTime=2
        