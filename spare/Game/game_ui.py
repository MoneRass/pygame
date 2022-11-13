import pygame
from menu import *

class Stamina_bar:
    def __init__(self,stamina,max_stamina):
        
        self.stamina = stamina
        self.max_stamina = max_stamina

    def draw(self, stamina):
        ratio = self.stamina / self.max_stamina                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        stamina_box = pygame.Rect(0,screen_height-10,screen_width*ratio,10)
        #update with new health
        self.stamina = stamina
        #calculate health ratio
        pygame.draw.rect(screen, 'green', stamina_box,0)
