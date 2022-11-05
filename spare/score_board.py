import pygame
from save import *
from map import *
from menu import *

class name_box():
    def __init__(self, name,pos):
       
        self.fonts = pygame.font.Font('font/Liquefy.otf', 150)

    def name(self,name,pos):
        self.display_name=fonts.render(name, True,(255,255,255))
        screen.blit(self.display_name, (50,20+pos))

        