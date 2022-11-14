from venv import create
import pygame
from Hunter import Hunter
import random
import math
class Flying_Bat(pygame.sprite.Sprite):
    def __init__(self, pos, surface):

        super().__init__()

        self.speed=9
        self.image = pygame.Surface((40, 56))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.image=surface
        self.sinY=3.14
        self.speed_up=0
    def animation():
        pass
#why u dont close the screennnnnnnnnnnnnnn
    def update(self, bat_shift,hit):
        self.rect.x-=(self.speed+self.speed_up)+bat_shift
        #self.rect.y+=math.sin(self.sinY)
        if(self.rect.x<=0):
            self.rect.x=5000
            self.rect.y=random.randint(3,13)*60
            self.speed_up+=0.1
        if(hit==True):
            self.remove()


    def dead(self):
        self.remove()
        print('kill')
        
       
       
    

