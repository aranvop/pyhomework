import pygame
from set import *
class Timer:
    def __init__(self,duration,func=None):
        self.duration=duration
        self.func=func
        self.startTime=0
        self.active=False
    def active(self):
        self.active=True
        self.startTime=pygame.time.get_ticks()

    def deactive(self):
        self.active=True
        self.startTime=0
    
    def update(self):
        currentTime=pygame.time.get_ticks()
        if currentTime-self.startTime>=self.duration:
            self.deactive()
            if self.func:
                self.func()
