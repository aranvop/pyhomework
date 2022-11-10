import pygame
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()
#gameArea=pygame.Rect(-10, -10, 800, 600)
dt=clock.tick(60)/1000
enemylist=[]
playerlist=[]
power=200
rang1=20
ifpowerChange=False
score=0
playerhealth = 10.0
playerpos=(400,600)
mupath='./music/1.mp3'
# enemytype={
#     1:'1',
#     2:'2',
#     3:'3',
#     4:'4',
# }