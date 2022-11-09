import pygame ,sys
from player import Player
from level import Level
WIN_wid=800
WIN_hei=600




# def main():
#     #pl1=Player()
#     #pygame.transform.smoothscale(pygame.image.load('./resource/player/pl00/floatGun.png'),(120,24))
#     pygame.init()
#     player=pygame.image.load('./pl1.png')
#     #player1=pygame.image.save
#     #pl1=pygame.Surface.set_clip() 
#     screen=pygame.display.set_mode((WIN_wid,WIN_hei))
#     screen.fill((55,55,250))
#     bg1=pygame.image.load('./moon.png')
#     newbg1=pygame.transform.scale(bg1,(800,600),)
#     pygame.display.set_caption("py大作业")
#     #font=pygame.font.Font('./font.ttf',20)
#     #text =font.render('111',True,(0,0,0))
#     bg2=pygame.image.load('./bg2.png')
#     bg2=pygame.transform.scale(bg2,(WIN_wid,WIN_hei-50))
#     while True:
        
#         screen.blit(newbg1,(0,0))
#         # screen.blit(text,(0,0))
#         # screen.blit(text,(20,20))
#         screen.blit(bg2,(0,50))
#         screen.blit(player,(0,0))
#         pygame.display.update()
#         eventList=pygame.event.get()
#         for event in eventList:
#             if event.type==pygame.QUIT:
#                 exit()
                
#             #elif eve
#     print('yes')
# if  __name__== '__main__':
#    main()

class Game:
    def __init__(self) :
        pygame.init()
        self.screen=pygame.display.set_mode((800,600))
        self.clock=pygame.time.Clock()
        self.level=Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt=self.clock.tick(60)/1000
            self.level.run(dt)
            if self.level.player.health<0:
                sys.exit()
            pygame.display.update()
if __name__=='__main__':
    game=Game()
    game.run()
