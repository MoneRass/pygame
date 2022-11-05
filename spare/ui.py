import pygame

BAR_HEIGHT = 20
HEALTH_WIDTH = 200
STAMINA_WIDTH = 160

class UI:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_WIDTH,BAR_HEIGHT)
        self.stamina_bar_rect = pygame.Rect(10,30,STAMINA_WIDTH,BAR_HEIGHT)

    def display(self,player):
        pygame.draw.rect(self.display_surface,'black',self.health_bar_rect)