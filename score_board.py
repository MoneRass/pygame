import pygame,sys

from map import *
from menu import *


class name_box():
    def __init__(self, name,score,pos):
       
        self.fonts = pygame.font.Font('font/Liquefy.otf', 150)
        self.display_name=fonts.render(name, True,(255,255,255))
        self.display_score = fonts.render(score, True,(255,255,255))
        screen.blit(self.display_name, (50,pos))
        screen.blit(self.display_score, (screen_width/2,pos))

